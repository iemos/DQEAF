#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description:
# Create a PE which pop a MessageBox
# with the message "Hello World"
# fetch detail : https://lief.quarkslab.com/doc/tutorials/02_pe_from_scratch.html

from lief import PE

# First we have to create a Binary :
binary32 = PE.Binary("pe_from_scratch", PE.PE_TYPE.PE32)

# The first parameter is the binary’s name and the second one
# is the type: PE32 or PE64 (see PE_TYPE). The Binary‘s constructor
# creates automatically DosHeader, Header, OptionalHeader an empty DataDirectory.
#
# Now that we have a minimal binary, we have to add sections.
# We will have a first section holding assembly code (.text)
# and a second one containing strings (.data):

# A MessageBoxA is composed of a title and a message.
# These two strings will be stored in the .data as follows:
title = "LIEF is awesome\0"
message = "Hello World\0"

data = list(map(ord, title))
data += list(map(ord, message))
code = [
    0x6a, 0x00,  # push 0x00 uType
    0x68, 0x00, 0x20, 0x40, 0x00,  # push VA(title)
    0x68, 0x10, 0x20, 0x40, 0x00,  # push VA(message)
    0x6a, 0x00,  # push 0 hWnd
    0xFF, 0x15, 0x54, 0x30, 0x40, 0x00,  # call MessageBoxA
    0x6A, 0x00,  # push 0 uExitCode
    0xFF, 0x15, 0x4C, 0x30, 0x40, 0x00  # call ExitProcess
]

section_text = PE.Section(".text")
section_text.content = code
section_text.virtual_address = 0x1000

section_data = PE.Section(".data")
section_data.content = data
section_data.virtual_address = 0x2000

section_text = binary32.add_section(section_text, PE.SECTION_TYPES.TEXT)
section_data = binary32.add_section(section_data, PE.SECTION_TYPES.DATA)

print(section_text)
print(section_data)

binary32.optional_header.addressof_entrypoint = section_text.virtual_address

kernel32 = binary32.add_library("kernel32.dll")
kernel32.add_entry("ExitProcess")

user32 = binary32.add_library("user32.dll")
user32.add_entry("MessageBoxA")

ExitProcess_addr = binary32.predict_function_rva("kernel32.dll", "ExitProcess")
MessageBoxA_addr = binary32.predict_function_rva("user32.dll", "MessageBoxA")
print("Address of 'ExitProcess': 0x{:06x} ".format(ExitProcess_addr))
print("Address of 'MessageBoxA': 0x{:06x} ".format(MessageBoxA_addr))

builder = PE.Builder(binary32)
builder.build_imports(True)
builder.build()
builder.write("pe_from_scratch.exe")
