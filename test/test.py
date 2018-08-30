import os
import shutil
from collections import OrderedDict

from gym_malware.envs.utils import interface

dd = OrderedDict([('Backdoor.Win32.PcClient.ovm', {'actions': [], 'evaded': False}), ('Backdoor.Win32.PcClient.fgn',
                                                                                      {'actions': ['ARBE', 'ARS'],
                                                                                       'evaded': True,
                                                                                       'evaded_sha256': 'fe92c286819f7cfca1b79e863e178e1c507e06d57509798d945c493c330af7e1'}),
                  ('Backdoor.Win32.Mhtserv.a', {'actions': ['ARI'], 'evaded': True,
                                                'evaded_sha256': 'eaea436f95031bac3d3041f0bfd25200d9c3b9d42c4fcdd45ad6c248dfff61ea'}),
                  ('Backdoor.Win32.Poison.bsb', {
                      'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'RS', 'ARBE', 'ARS', 'RS',
                                  'ARBE', 'ARBE', 'ARBE', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARS', 'ARS',
                                  'ARBE', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARS', 'RS', 'ARS', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Rbot.ein', {
        'actions': ['ARS', 'RS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARI',
                    'ARS', 'ARBE', 'ARI', 'RS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'RS',
                    'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARI', 'RS', 'ARBE',
                    'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS',
                    'ARS', 'ARBE', 'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.ihj', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE',
                    'ARI', 'RS', 'ARBE', 'RS', 'ARBE', 'ARI', 'ARS', 'RS', 'RS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI',
                    'ARS', 'ARBE', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'RS', 'RS', 'ARS', 'RS',
                    'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARS', 'RS', 'ARI', 'RS', 'ARI', 'ARBE', 'RS',
                    'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fyo',
                                                      {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                       'evaded_sha256': '462f195b35e561d77cad5a2801f1dd0c054c33d9cb26da6751317c90c476bc0c'}),
                  ('Backdoor.Win32.Nethief.16', {
                      'actions': ['RS', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARBE', 'RS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE',
                                  'ARBE', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'ARS', 'ARI',
                                  'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS', 'RS', 'ARBE', 'ARBE', 'ARS',
                                  'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARS', 'ARI', 'RS', 'ARS', 'ARBE', 'RS', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PoeBot.a', {
        'actions': ['ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARI', 'RS', 'ARI',
                    'ARS', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'RS', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARI', 'ARI', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'RS',
                    'ARBE', 'RS', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'RS',
                    'RS', 'ARS', 'ARI', 'RS'], 'evaded': False}), ('Backdoor.Win32.Pahador.av', {
        'actions': ['ARI', 'ARBE', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARBE', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARBE',
                    'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS',
                    'RS', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'RS', 'ARI',
                    'RS', 'ARBE', 'RS', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.Poison.crx', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARI',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'RS', 'ARI', 'ARI', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS',
                    'ARS', 'RS', 'ARS', 'RS', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Kbot.s', {
        'actions': ['RS', 'ARBE', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE', 'RS', 'ARS', 'ARBE', 'RS',
                    'ARBE', 'RS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARS', 'RS', 'ARS',
                    'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS',
                    'ARBE', 'ARBE', 'ARI', 'ARBE', 'RS', 'RS', 'RS', 'ARBE', 'ARBE', 'RS', 'ARBE', 'RS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARBE', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.adi', {
        'actions': ['ARI', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '78f952a8ee39320ff54808c9d178327dbe119e57c0e5edf94ab29c3f4724d55e'}), (
                  'Backdoor.Win32.Masot.b', {
                      'actions': ['ARBE', 'ARS', 'ARBE', 'ARI', 'RS', 'RS', 'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE',
                                  'RS', 'ARI', 'ARS', 'ARI', 'RS', 'RS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARBE', 'RS',
                                  'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'RS', 'RS', 'ARS',
                                  'ARBE', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARBE', 'RS', 'ARS', 'ARI',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.iuw', {
        'actions': ['ARS', 'RS', 'ARI', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARBE', 'RS', 'RS', 'ARI', 'ARS',
                    'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARS', 'RS', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARI'], 'evaded': True,
        'evaded_sha256': '472c753ab57b680a9b7713bec9ec79b8d9423f7bf84001972a03a70ab8141957'}), (
                  'Backdoor.Win32.Optix.Pro.di', {
                      'actions': ['ARBE', 'ARI', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARS', 'RS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS',
                                  'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'RS', 'ARI', 'RS', 'RS',
                                  'RS', 'ARI', 'ARS', 'RS', 'ARS', 'ARBE', 'ARBE', 'RS', 'RS', 'ARI', 'ARI', 'ARBE',
                                  'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'ARI', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.mkp',
                                                               {'actions': ['ARI'], 'evaded': True,
                                                                'evaded_sha256': 'd01dc4f4f04d22dda3f330c31145aa27ada00e2a9054cd2a78a03f0dcd4f8e31'}),
                  ('Backdoor.Win32.Poison.bfk', {
                      'actions': ['ARBE', 'ARBE', 'RS', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARS', 'RS', 'ARI', 'RS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE',
                                  'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'RS', 'ARI',
                                  'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS', 'ARBE', 'ARS',
                                  'RS', 'ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'RS', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.gny', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'f8545c33c345ca0f065f02bca21f4b9f7e740f9c45f57d97753cd2dabba74b3f'}),
                  ('Backdoor.Win32.PcClient.ejl', {
                      'actions': ['RS', 'ARI', 'ARBE', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARS'], 'evaded': True,
                      'evaded_sha256': '2ec70dddd17b6fa22b8e76acce76ee789b58bdbb1c1ec076884c82191ebf1e44'}), (
                  'Backdoor.Win32.Poison.dre', {
                      'actions': ['RS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARI', 'RS',
                                  'ARI', 'RS', 'ARI', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'RS', 'RS',
                                  'ARBE', 'ARS', 'RS', 'RS', 'ARS', 'RS', 'RS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'RS',
                                  'ARBE', 'ARBE', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'RS',
                                  'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ejp', {
        'actions': ['RS', 'ARBE', 'RS', 'ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'RS', 'ARI', 'RS',
                    'ARI', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'RS', 'RS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'RS', 'ARS',
                    'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARS'], 'evaded': True,
        'evaded_sha256': '4b07714f3629d6ec428befebd8ff51b1e966c20f1955f74c41f5191817d362c9'}), (
                  'Backdoor.Win32.PcClient.ctx', {
                      'actions': ['ARS', 'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'RS', 'ARBE', 'ARS',
                                  'RS', 'RS', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE',
                                  'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARBE', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARBE', 'ARI'], 'evaded': True,
                      'evaded_sha256': '9c5ca48e2756ab591b2663d15f99290b4eead1d3ba6c0c590b09c8d37f3fcc50'}), (
                  'Backdoor.Win32.Poison.ajub', {'actions': ['RS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
                                                 'evaded_sha256': '17e89abc6ccdb8d3fe62abc8dc378756cd3216eee11a448a53107bb5acc3abee'}),
                  ('Backdoor.Win32.PcClient.dnq', {'actions': ['ARI'], 'evaded': True,
                                                   'evaded_sha256': 'ea2d66918fda13b854476890d679ea755a3b76a06c3853f41210ab750c578b89'}),
                  ('Backdoor.Win32.Netsnake.f', {
                      'actions': ['ARI', 'RS', 'ARBE', 'RS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI',
                                  'ARS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'RS', 'RS', 'ARI', 'ARS', 'ARI', 'ARS',
                                  'ARI', 'RS', 'RS', 'RS', 'ARI', 'RS', 'ARBE', 'ARI', 'ARI', 'ARS', 'RS', 'RS', 'ARBE',
                                  'RS', 'ARS', 'ARI', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARS', 'ARBE', 'ARI', 'RS', 'ARI',
                                  'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARS'], 'evaded': False}), (
                  'Backdoor.Win32.PcClient.mvx', {
                      'actions': ['ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'RS', 'RS', 'RS', 'ARBE', 'RS', 'ARS', 'ARS', 'RS',
                                  'ARBE', 'ARI', 'RS', 'RS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'RS', 'ARI',
                                  'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARI',
                                  'RS', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'RS', 'ARI', 'ARS', 'RS', 'ARBE', 'RS', 'ARI',
                                  'ARS', 'ARBE', 'ARBE', 'RS', 'RS', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.juz', {
        'actions': ['RS', 'ARI', 'RS', 'ARI', 'RS', 'ARBE', 'RS', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARBE', 'RS',
                    'ARBE', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARBE', 'RS', 'ARI', 'RS', 'ARS',
                    'ARS', 'ARI', 'RS', 'ARBE', 'RS', 'ARBE', 'RS', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARS',
                    'RS', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'ARS', 'RS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Poison.dfm',
                                                                    {'actions': ['RS', 'ARS'], 'evaded': True,
                                                                     'evaded_sha256': '9e6b87d98e7469cf04dc64bebf7aa3b9a51e6b2d78c85634bc64919068a3b0b7'}),
                  ('Backdoor.Win32.Nuclear.iz', {'actions': ['RS', 'RS', 'RS', 'ARS'], 'evaded': True,
                                                 'evaded_sha256': 'e7dc72f5c1372d67c0e77ef24876d713e34b482b77e9bc523967319927a7ad68'}),
                  ('Backdoor.Win32.Hupigon.zhv', {
                      'actions': ['RS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARBE',
                                  'ARS', 'RS', 'ARI', 'ARS', 'ARBE', 'ARI', 'RS', 'ARI', 'RS', 'RS', 'ARI', 'RS', 'RS',
                                  'RS', 'ARS', 'RS', 'ARI', 'RS', 'RS', 'RS', 'ARS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARI',
                                  'ARS', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS',
                                  'ARS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARI', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Kbot.fd', {
        'actions': ['ARBE', 'ARS', 'ARBE', 'ARI', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARBE', 'RS', 'RS', 'ARI', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'ARBE',
                    'ARI', 'ARBE', 'ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE',
                    'ARBE', 'RS', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.ofy', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARBE', 'RS', 'ARBE',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'ARI', 'ARBE', 'ARBE',
                    'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'RS', 'RS', 'RS', 'ARBE', 'ARS',
                    'ARS'], 'evaded': True,
        'evaded_sha256': 'e425858e7b9b4d10bb8bfca6b4588d64aeade5b06b6d614eaf43eb6f545ae18e'}), (
                  'Backdoor.Win32.Kbot.ee', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'ARI', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARBE', 'RS', 'ARBE', 'ARBE', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'RS',
                                  'RS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bvt', {
        'actions': ['ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'RS', 'RS', 'ARI', 'RS', 'ARBE',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARI',
                    'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE',
                    'ARS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'RS', 'ARBE', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.aec', {
        'actions': ['ARS', 'RS', 'ARBE', 'ARBE', 'RS', 'ARS'], 'evaded': True,
        'evaded_sha256': '3dfe61aa969ee28d7a4f239b10edb025c476e167b2e905e3947c00d289aa2ce3'}), ('Backdoor.Win32.Jaan.u',
                                                                                                {'actions': ['ARI',
                                                                                                             'RS',
                                                                                                             'ARS',
                                                                                                             'RS',
                                                                                                             'ARBE',
                                                                                                             'RS',
                                                                                                             'ARI',
                                                                                                             'RS', 'RS',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'RS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'RS',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'ARBE',
                                                                                                             'RS', 'RS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'RS', 'RS',
                                                                                                             'ARS',
                                                                                                             'RS',
                                                                                                             'ARI',
                                                                                                             'ARBE',
                                                                                                             'RS', 'RS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARBE'],
                                                                                                 'evaded': False}), (
                  'Backdoor.Win32.PcClient.deh', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '54e19088d56a5147291f05b169380aa2e1a4fbe325bfe5f8963498cc3021d5d2'}),
                  ('Backdoor.Win32.PcClient.hwm', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARBE', 'ARI',
                                  'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Masteseq.bh', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARS', 'RS', 'ARI', 'ARI', 'RS', 'ARS', 'RS',
                    'RS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARBE',
                    'ARBE', 'ARI', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.eqw',
                                                                    {'actions': ['ARBE', 'ARI'], 'evaded': True,
                                                                     'evaded_sha256': 'c4ca904074b070e0ca0b7f0c61e0fff0c2bb1b1bdec674559dc3074bb52d092f'}),
                  ('Backdoor.Win32.MiniCommander.10.d', {
                      'actions': ['ARS', 'ARBE', 'RS', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARI',
                                  'ARS', 'RS', 'ARI', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARI',
                                  'ARS', 'ARI', 'ARBE', 'RS', 'ARBE', 'ARBE', 'ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Kbot.oq', {
        'actions': ['ARS', 'ARBE', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'ARI', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARI', 'RS', 'RS', 'RS', 'ARBE',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'RS',
                    'ARI', 'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE',
                    'ARI', 'ARI', 'ARI', 'RS'], 'evaded': False}), ('Backdoor.Win32.Nuclear.br', {
        'actions': ['ARBE', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS', 'ARS',
                    'RS', 'RS', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'ARS', 'RS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE',
                    'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARI',
                    'ARBE', 'ARS', 'ARS', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.etz', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARI'], 'evaded': True,
        'evaded_sha256': '290e9a2f3e4d5960f074faa158c5f9d767a2c1f7c85683feca4c19062d177d86'}), (
                  'Backdoor.Win32.InCommander.12', {
                      'actions': ['ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'RS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARI', 'RS', 'ARBE',
                                  'RS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '20e81350d06bf63edf9ebef9925be20b6cfffd336e1a5cefc84513087cb125df'}), (
                  'Backdoor.Win32.PcClient.grq', {'actions': ['RS', 'ARI', 'ARS', 'ARI', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '8b657e2f54e203e15faea085b8486c3ec732cdc3b8769681929e07accdf24423'}),
                  ('Backdoor.Win32.PcClient.gok', {
                      'actions': ['ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARS',
                                  'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS',
                                  'ARS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARBE', 'RS', 'ARS',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.ctw', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARI', 'RS',
                    'ARI', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARBE', 'RS',
                    'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARBE',
                    'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.pmh', {
        'actions': ['ARI', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                    'RS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARBE', 'RS', 'ARS'], 'evaded': True,
        'evaded_sha256': '9663d7b9a94bb33f7f7a654775298a1dcf71d0f9e91a7fb978504b83577326e0'}), (
                  'Backdoor.Win32.PcClient.jak', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'RS', 'ARBE', 'RS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARI',
                                  'ARS', 'ARBE', 'RS', 'RS', 'ARBE', 'RS', 'ARBE', 'RS', 'RS', 'ARBE'], 'evaded': True,
                      'evaded_sha256': 'd61fb20f8c78681828e52beca32140dab2ab5656f6af528f731331c00d45993b'}), (
                  'Backdoor.Win32.PcClient.eqm', {'actions': ['ARI', 'ARI', 'ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '0796b7456c33d6d22bf8d64e14b3e05108888b622aba12a68dfc0813dd8929c3'}),
                  ('Backdoor.Win32.PcClient.fns', {'actions': ['ARI'], 'evaded': True,
                                                   'evaded_sha256': 'ecf0a1b05bc29283ad22c8e437fedb8992b0affaba8c387a5876e83446d31e43'}),
                  ('Backdoor.Win32.Optix.04.f', {
                      'actions': ['ARBE', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARI',
                                  'ARBE', 'RS', 'RS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS',
                                  'ARBE', 'ARS', 'ARI', 'ARI', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARBE', 'RS',
                                  'RS', 'RS', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARI',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.emy', {
        'actions': ['ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARS',
                    'ARBE', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARI'], 'evaded': True,
        'evaded_sha256': 'c31cf54c93288fb7158b665fd87439f957a89d436ac2fd1d1842b52008342f05'}), (
                  'Backdoor.Win32.Inject.dv', {
                      'actions': ['ARBE', 'RS', 'ARBE', 'ARBE', 'RS', 'ARBE', 'ARBE', 'RS', 'ARBE', 'RS', 'ARI', 'ARBE',
                                  'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'RS',
                                  'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARI', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARBE', 'ARS',
                                  'ARBE', 'RS', 'ARI', 'ARI', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARS'], 'evaded': False}), ('Backdoor.Win32.MServ.b',
                                                              {'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARS'],
                                                               'evaded': True,
                                                               'evaded_sha256': '3832909e90621135f8bea3598af6a9825bd304d4618979106839a66887046eba'}),
                  ('Backdoor.Win32.MoSucker.hq', {
                      'actions': ['ARI', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'RS', 'ARS', 'ARI', 'ARI',
                                  'ARBE', 'RS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS',
                                  'ARI', 'ARBE', 'ARI', 'RS', 'RS', 'RS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fxt', {
        'actions': ['RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI',
                    'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARI', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARI', 'ARI',
                    'ARBE', 'RS', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARS', 'ARBE', 'ARS', 'ARI',
                    'ARI'], 'evaded': True,
        'evaded_sha256': 'be2712f0c8e9faf022a179781609c98097efdc0cf65c5afaf7fc8a9e81d93af1'}), (
                  'Backdoor.Win32.Poison.ddl', {
                      'actions': ['ARBE', 'ARBE', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARBE', 'RS', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'RS', 'ARI',
                                  'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARI',
                                  'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARBE', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.aanf', {
        'actions': ['RS', 'ARBE', 'ARI', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARI',
                    'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'RS', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS', 'ARI',
                    'ARS', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI',
                    'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARBE', 'RS', 'ARI', 'ARI', 'ARBE',
                    'RS', 'RS', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.ltd', {
        'actions': ['ARS', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARS',
                    'ARI', 'RS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jig', {
        'actions': ['ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS'], 'evaded': True,
        'evaded_sha256': 'b1f561a3c9968b8e468cbc866bb23856d2e904c01deb7e0a72f262c9371bf0a3'}), (
                  'Backdoor.Win32.PcClient.eqt', {
                      'actions': ['RS', 'ARS', 'ARBE', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'ARI', 'ARBE', 'RS', 'ARS',
                                  'ARI', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS',
                                  'ARBE', 'RS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARI', 'ARI', 'ARBE',
                                  'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ans',
                                          {'actions': ['ARS', 'ARBE', 'ARI'], 'evaded': True,
                                           'evaded_sha256': 'aeb9628047b57270527cf65c742231bf2d4f4edf7638fbb3b183a5ce44a7b6eb'}),
                  ('Backdoor.Win32.Jacktron.20', {'actions': ['ARBE', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': 'dd464c962ec0e39eea96fdb03725d757cdf8dbd28c01cd25f36da56c52e10853'}),
                  ('Backdoor.Win32.PcClient.ore', {
                      'actions': ['ARS', 'ARI', 'ARBE', 'ARBE', 'RS', 'RS', 'ARI', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARI',
                                  'RS', 'ARI', 'RS', 'ARI', 'ARBE', 'RS', 'ARI', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'ARS',
                                  'ARBE', 'ARI', 'ARS', 'ARI', 'RS', 'ARBE', 'RS', 'RS', 'RS', 'ARS', 'ARI', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ivw', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE', 'RS', 'ARS',
                    'ARI', 'ARS', 'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARI', 'ARI', 'RS', 'RS', 'ARI',
                    'ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.ajh', {
        'actions': ['ARI', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '5a41b352ff816f9c855579fcf801f44c5591631242133ee353c7a776e7d4cb31'}), (
                  'Backdoor.Win32.PcClient.cy', {
                      'actions': ['ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS',
                                  'ARS'], 'evaded': True,
                      'evaded_sha256': 'f694a57c1969ddae821d5b50515d1d0fb2f7b26b7b059ed310738e11b66b63d9'}), (
                  'Backdoor.Win32.PcClient.jnh', {'actions': ['ARI', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '536be31d23be57d90aa8de847a02085075f250ff2da82e667a407b55accad2e9'}),
                  ('Backdoor.Win32.PcClient.dtl', {'actions': ['ARBE', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                   'evaded_sha256': 'dcece68a163432833650aa46eefe9b4b828287c24d95e0ac09b9940c76ad5ccc'}),
                  ('Backdoor.Win32.PcClient.poh', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS',
                                  'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'ARBE',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'RS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.luv', {
        'actions': ['ARI', 'ARI', 'RS', 'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARI', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS',
                    'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARBE',
                    'RS', 'ARBE', 'ARI', 'RS'], 'evaded': False}), ('Backdoor.Win32.Poison.dnx',
                                                                    {'actions': ['ARS'], 'evaded': True,
                                                                     'evaded_sha256': '89e61d75c71cba5cbee5740d11cccce40c574918c5b90384a176ba442f5e5107'}),
                  ('Backdoor.Win32.NinjaSpy.d', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'ARS', 'ARI', 'ARI', 'ARBE',
                                  'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARS', 'ARBE', 'ARS',
                                  'ARBE', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.gmg', {
        'actions': ['RS', 'ARS', 'ARI', 'RS', 'RS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'RS', 'ARI', 'RS',
                    'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARI', 'RS',
                    'ARBE', 'ARI', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.hys', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'ARI', 'ARBE',
                    'RS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'RS', 'ARS',
                    'ARS', 'ARBE', 'ARI', 'RS'], 'evaded': False}), ('Backdoor.Win32.Lithium.c',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'f64aa5d528792718003d17a08af15f89e18a75a3b4b2f5b7e3ce7f7d2ec2afef'}),
                  ('Backdoor.Win32.Hupigon.zok',
                   {'actions': ['ARI', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS'], 'evaded': True,
                    'evaded_sha256': '9299234dc7d5cb4a971611afd4698a0b4563dc079b5f38c8806e5deec2d43901'}), (
                  'Backdoor.Win32.PcClient.rtr',
                  {'actions': ['RS', 'RS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'ARS', 'ARS'], 'evaded': True,
                   'evaded_sha256': '259e81b671065d4d82bbb40b0b56a647267e02ea95e71a820eadfc5544292417'}), (
                  'Backdoor.Win32.IRCBot.hrq', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'RS', 'RS', 'ARS', 'RS',
                                  'ARBE', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'RS', 'RS',
                                  'ARS', 'ARBE', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'RS', 'ARI', 'RS',
                                  'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.NinjaSpy.b', {
        'actions': ['RS', 'ARBE', 'ARS', 'RS', 'RS', 'ARI', 'RS', 'ARI', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARI',
                    'ARS', 'RS', 'RS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'be18819b240fa97fca5335c315819b9497d5c6b59ed71bcb1b78a01102ca53b8'}), (
                  'Backdoor.Win32.PcClient.gxm', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '831d93e0fa8cb2f9aed08bd2823b4f9e1379e74bfb680f3635272d63980a8891'}),
                  ('Backdoor.Win32.MoSucker.30.ac', {
                      'actions': ['RS', 'RS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
                      'evaded_sha256': '0684c33c41bf57fe5b6d40fb688ab80d4896a47e9b7290907da62c66a3201d56'}), (
                  'Backdoor.Win32.IRCBot.hsg', {'actions': ['ARI', 'ARI', 'ARI'], 'evaded': True,
                                                'evaded_sha256': '50c6b4248d115667e07ec4c135869054b00c073363101c68c91807f4d3c8a394'}),
                  ('Backdoor.Win32.PcClient.gav', {
                      'actions': ['ARBE', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARBE',
                                  'ARS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'RS',
                                  'ARI', 'RS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '872b7ef6543834104113a516da79f162982af377e729d83287d72b9a1c74bceb'}), (
                  'Backdoor.Win32.Hupigon.zid', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'RS', 'RS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'RS',
                                  'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'RS',
                                  'ARBE', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.hwa', {
        'actions': ['ARS', 'ARBE', 'RS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS',
                    'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '44f4c6b26ccab088ddaaa72696c88c61b4d3f33b046700afb2455159bd719574'}), (
                  'Backdoor.Win32.PcClient.eqa', {
                      'actions': ['RS', 'ARS', 'RS', 'RS', 'ARS', 'RS', 'ARI', 'ARS', 'ARI', 'ARBE', 'RS', 'RS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARI',
                                  'ARBE', 'ARS', 'RS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.buy',
                                          {'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARI'],
                                           'evaded': True,
                                           'evaded_sha256': 'cd872f3ef75980ae0ded0256c3f26afb8ae675af0dcb3cf23a3b2af80aab3453'}),
                  ('Backdoor.Win32.PcClient.za', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARI', 'RS',
                                  'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARI', 'RS',
                                  'ARBE', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARI',
                                  'ARI', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS', 'RS', 'ARI', 'ARI',
                                  'ARS', 'RS', 'ARI', 'RS', 'ARI', 'RS', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Oblivion.01.a', {
        'actions': ['ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '1c886564cb1997424289caa3ff876b261c6f4deedaa6cb81e4eff8d6c2238d8d'}), (
                  'Backdoor.Win32.PcClient.gtw',
                  {'actions': ['RS', 'ARBE', 'ARI', 'ARI', 'RS', 'ARS', 'ARI'], 'evaded': True,
                   'evaded_sha256': '270f48c2c81f2f233810a2dbc02b33e19e738a74c7df75d6396eade6b831672b'}), (
                  'Backdoor.Win32.PcClient.ggk', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '76e7ba27b5ba128694d55028618133de93bd4804df47cfa1aef1644ce82f3760'}),
                  ('Backdoor.Win32.PcClient.cbr', {
                      'actions': ['ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'RS', 'ARI', 'RS', 'ARS', 'RS', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI',
                                  'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.Masot.f', {
        'actions': ['ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'RS',
                    'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI',
                    'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARBE', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.idj', {
        'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARI', 'ARS', 'ARBE', 'RS', 'ARBE', 'RS', 'RS', 'RS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS',
                    'ARBE', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'RS', 'ARI', 'RS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.MiniCommander.10.c', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '72fa0464cc9ed7d2460acae859b37b9feeef7b2d7cda586ee7084585c4b42cf6'}), (
                  'Backdoor.Win32.Optix.Pro.fw', {
                      'actions': ['ARBE', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS', 'ARI', 'RS', 'RS',
                                  'ARBE', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                                  'ARBE', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'RS', 'RS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.Nepoe.co', {
        'actions': ['ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': 'b6d7a95731b676fedfc705f021227b1b0df058f8290b0fe1bf1ef58f33c20f40'}), (
                  'Backdoor.Win32.PcClient.agu', {
                      'actions': ['RS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS',
                                  'ARS', 'ARI', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARS', 'ARI', 'RS', 'ARI', 'ARBE',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bvv', {'actions': ['ARI'], 'evaded': True,
                                                                          'evaded_sha256': '1dd5b646aa96dfcf84d9abf516485e3172b0183180fef1aa556d744e6c6f1760'}),
                  ('Backdoor.Win32.PcClient.fsp', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARBE', 'RS', 'ARS', 'RS', 'ARI',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'cc15cdf3ece9c0087986e70f047f7a5a9f1fb7dfcaa0944a759a7aca71aedaf9'}), (
                  'Backdoor.Win32.PcClient.ane', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '565a182ff1f0e75fd2d32cb25962c1adaac4d729d3aa845a05b3b899f0dfcecd'}),
                  ('Backdoor.Win32.PcClient.efj', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '2a7ca43737b56a34410d607035b6823f69e649066658329f8b0e7719c2355d88'}),
                  ('Backdoor.Win32.IRCBot.gmh', {
                      'actions': ['ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE',
                                  'RS', 'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARBE', 'RS', 'ARI', 'ARI', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARI', 'RS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.NetCrack.13.h', {
        'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'b115efb123a0bdd8043a05ff14fda5cb467a261c569b18ebc6f83484f8685b7c'}), (
                  'Backdoor.Win32.PcClient.cjk', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARBE',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'RS', 'RS', 'ARBE', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARBE',
                                  'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fjg', {
        'actions': ['ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE',
                    'RS', 'RS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.MoSucker.21.b', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARBE', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'RS', 'ARI',
                    'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS',
                    'ARI', 'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jkr',
                                                                      {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                                       'evaded_sha256': '7b362aa1ff134a98fac980f32a175280ed2e52fb177b8b9d5e446fa887a137f8'}),
                  ('Backdoor.Win32.PcClient.pll', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARBE',
                                  'ARI', 'ARI', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE',
                                  'ARS', 'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.yma', {
        'actions': ['ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'RS', 'RS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nepoe.en', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARS', 'RS', 'RS', 'ARI', 'RS', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARS', 'RS', 'ARS', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': 'bf29100c1204c6722ec828f6430f5b52e1e12ed53074ed9af6702685c82b38d6'}), (
                  'Backdoor.Win32.PcClient.dkx', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS',
                                  'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARBE',
                                  'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARBE', 'ARBE',
                                  'ARS', 'RS', 'ARBE', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.nil', {'actions': ['ARI', 'ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'ba3be0cd06a5f0542193f6a3f60600c0e3a27dd275cc3c64b45e04fadcad6bdd'}),
                  ('Backdoor.Win32.PcClient.ap', {
                      'actions': ['RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS'], 'evaded': True,
                      'evaded_sha256': '1bad6c5097ee2f6c1ea5d27509ef25a6e4cd1bac4822eab75fd979599941123a'}), (
                  'Backdoor.Win32.PcClient.cep', {'actions': ['RS', 'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': 'fbf9f4d56b53bb57c65347883416ff4140fa6668459f054923d7705ba6d5de28'}),
                  ('Backdoor.Win32.PcClient.dup', {
                      'actions': ['ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE',
                                  'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'RS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bwv', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'b90d8b8533da388542fbcb4663ea261d886aa7092aa3bf2308defd4b23df6b3c'}),
                  ('Backdoor.Win32.PcClient.ewd', {'actions': ['ARS', 'ARS', 'RS', 'ARS'], 'evaded': True,
                                                   'evaded_sha256': '65ee0b0a267dcc7d0d2e3f908767273b3524c146ccfff6be7818b08977bedb27'}),
                  ('Backdoor.Win32.IRCBot.ghk', {
                      'actions': ['RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Kmedor', {
        'actions': ['RS', 'ARBE', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS',
                    'ARBE', 'RS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARBE', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.zah', {
        'actions': ['ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARI', 'RS', 'ARBE', 'ARI',
                    'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARBE',
                    'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '2503020092aeee957f1cc67609442a57910d255c6a186b1cef710ab2905f4663'}), (
                  'Backdoor.Win32.PcClient.byc', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '48c182a26cdcf2818e2e3d9fa3433cb1fab7da22fd9a78432fb4130f1ecd2a85'}),
                  ('Backdoor.Win32.Kokodoor.20.a', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARBE', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARBE', 'ARBE',
                                  'RS', 'ARS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARBE', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Nethief.12', {
        'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.edf', {
        'actions': ['RS', 'ARI', 'RS', 'RS', 'ARBE', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'RS', 'ARS', 'RS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '786134ebeaaf538aeb24d4d31fc169694ac41f95adf89bd33ad158049ca37c01'}), (
                  'Backdoor.Win32.InCommander.16.c',
                  {'actions': ['ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': True,
                   'evaded_sha256': 'f4050a609734e027779f84396a683127ec62aedc37eda99dd133617ed370d6db'}), (
                  'Backdoor.Win32.PcClient.jlp', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '9a745a00d9c46fd7b300370159edd45a085d860612e3c82a4b421d7b2a820974'}),
                  ('Backdoor.Win32.PcClient.bbl', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '241d7e2c7d5aebf572ddc28e53049c70c89b61458b7a9e84fe6f91e17d333320'}),
                  ('Backdoor.Win32.PcClient.eai',
                   {'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI'], 'evaded': True,
                    'evaded_sha256': 'a799c2d92445ebf19051acb20ccc34f4ea2a1c171e0d0d07193193b50ec26e65'}), (
                  'Backdoor.Win32.Poison.dbv', {
                      'actions': ['ARI', 'ARS', 'ARS', 'RS', 'ARBE', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                                  'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'RS', 'ARBE',
                                  'RS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Massaker.12.b', {
        'actions': ['ARI', 'ARI', 'ARS', 'RS', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS'], 'evaded': True,
        'evaded_sha256': '236c7e8a88dd3c58cd01faeb613a048eb3c71f176b818a2e7f3fbcedaeae8d91'}), (
                  'Backdoor.Win32.NTRootKit.122', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARBE',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'ARS', 'RS', 'RS', 'RS',
                                  'ARI', 'RS', 'RS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.Intruder.10.d', {
        'actions': ['ARI', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'RS',
                    'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS',
                    'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARBE',
                    'ARI', 'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Hupigon.zif', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'RS', 'RS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'RS',
                    'RS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.lne', {
        'actions': ['ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fjh', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE',
                    'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARS', 'ARBE', 'RS', 'ARS', 'RS', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'RS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.wk', {
        'actions': ['RS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '586db6fb4636c180159b96c513b497fd1e91c8719188cfbd29c046c7ceffd239'}), (
                  'Backdoor.Win32.PcClient.fjn',
                  {'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS'],
                   'evaded': True,
                   'evaded_sha256': '30e2e478213fe54cf7755da56521ac5e4fab737963351d764e248cc5e4d9f827'}), (
                  'Backdoor.Win32.PcClient.ejq', {'actions': ['ARBE', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': '8e263cf155fc585d08dcfb9577c4951d3098843092c858a771b9216f6a2602f4'}),
                  ('Backdoor.Win32.Poison.ckm', {
                      'actions': ['ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS',
                                  'ARI', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE', 'ARI',
                                  'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.KeyStart.ay', {
        'actions': ['ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'RS', 'RS', 'ARBE', 'ARI',
                    'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'RS',
                    'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARBE', 'RS', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Kbot.ea', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS', 'RS', 'RS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.ypq', {
        'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'], 'evaded': True,
        'evaded_sha256': '6c8a83443ba062878d7a474c62956b6aec5974998f5ebd4b2d010d7644a22d52'}), (
                  'Backdoor.Win32.PcClient.dvm', {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': 'c9283738a3bb181031b87c4a1f6b0c38c353e185579033e69b3b496a205b2faa'}),
                  ('Backdoor.Win32.PcClient.zbx', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'RS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS',
                                  'ARBE', 'RS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'c6e4e9a5a5e99d8eededd608b6c6a5e0e0e5ea2e36e6172b4f675ced8998d129'}), (
                  'Backdoor.Win32.PcClient.ivl', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'RS',
                                  'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARBE', 'RS', 'RS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ovp', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARI', 'ARS', 'RS', 'ARBE',
                    'ARI', 'ARI', 'RS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.hvw', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARS', 'ARBE', 'RS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'RS',
                    'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.pfh',
                                                                   {'actions': ['ARS', 'ARS', 'ARS'], 'evaded': True,
                                                                    'evaded_sha256': 'b043b6f3748858f073be430a500a4a9d5671679dc6850f490e7a573ae65e5703'}),
                  ('Backdoor.Win32.PcClient.plt',
                   {'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'RS', 'ARS'], 'evaded': True,
                    'evaded_sha256': '85ac334e0f136184cc0cbd23148ee9071fe7682ae31348332d653ea25573215b'}), (
                  'Backdoor.Win32.PcClient.has', {
                      'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'RS', 'ARBE',
                                  'ARI', 'ARBE', 'RS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Nepoe.bj', {
        'actions': ['RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARBE',
                    'RS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE',
                    'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '5c07ee8f9d8dc8344c1854a2c677f72733fa3b31c4f60d6eefb9944d5d272f5b'}), (
                  'Backdoor.Win32.PcClient.rp', {
                      'actions': ['ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'ARBE', 'RS', 'RS', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'RS', 'ARI', 'RS', 'RS', 'RS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dyj', {
        'actions': ['ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Poison.dhr', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.ggp', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARBE',
                    'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'RS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'RS',
                    'ARS'], 'evaded': True,
        'evaded_sha256': '2adbcf3cace81ff4263873bd922cbab2f395be6fa68035fe74ca1ea7dd1b3610'}), (
                  'Backdoor.Win32.PcClient.ime', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '08293ce1d83b370ad54a7eaf1b2f2d356b4c74740b144db6cc8d6664418515ce'}),
                  ('Backdoor.Win32.PcClient.opt', {
                      'actions': ['RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ewu', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.ky', {
        'actions': ['RS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARBE', 'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.cwd', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nepoe.c', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARBE', 'ARBE', 'RS', 'RS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARI', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.zjd', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.eep', {
        'actions': ['ARS', 'ARS', 'RS', 'ARBE', 'RS', 'RS', 'RS', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'RS', 'ARI',
                    'RS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'RS', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.JustJoke.21',
                                                               {'actions': ['ARS', 'ARBE', 'ARBE', 'ARS'],
                                                                'evaded': True,
                                                                'evaded_sha256': '7550812cc3342e5548eeffb3008ad411ea4c7c48dbde8e1ee58ff4e70516c4da'}),
                  ('Backdoor.Win32.Hupigon.zgq', {
                      'actions': ['ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                                  'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '8495b29bf842376fe36fb617338b7e82d1ca7cdb25dab1541f248974a71d448d'}), (
                  'Backdoor.Win32.Poison.alyb', {'actions': ['ARI'], 'evaded': True,
                                                 'evaded_sha256': '849a4f5ba756fd0ea7c98b5bb6ba2ca0ff8f85795d8b29e0019cc022a2662c34'}),
                  ('Backdoor.Win32.PcClient.lop', {
                      'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'RS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.eyf', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARS', 'ARI', 'ARBE', 'ARBE',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARBE', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jxq', {
        'actions': ['ARS', 'ARBE', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'RS', 'ARBE', 'RS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS',
                    'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Inject.gb', {
        'actions': ['ARS', 'ARS', 'ARBE', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARBE', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.epv', {
        'actions': ['ARBE', 'ARS', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARBE',
                    'ARS', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.MoSucker.20.a', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'RS', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.KeyStart.ae', {
        'actions': ['ARS', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'RS', 'RS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.zis', {
        'actions': ['ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '0f827918d0fc16de29c61744409bc13e623665a6b0261febffdd15267db226f6'}), (
                  'Backdoor.Win32.Nuclear.fl', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'RS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARI', 'RS', 'RS', 'RS',
                                  'RS', 'RS', 'ARBE', 'RS', 'ARS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.eaa', {
        'actions': ['RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'RS',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.mpj', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARBE',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Optix.04.c', {
        'actions': ['RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARBE', 'RS', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE',
                    'ARI', 'ARS', 'ARI', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.dok', {
        'actions': ['ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARI', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARBE', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.ygv',
                                                                      {'actions': ['ARS', 'ARI'], 'evaded': True,
                                                                       'evaded_sha256': '84bbbbe15dff8c5c9d1d911bab1bac76f771a22a1c153ba909283323dc718c1c'}),
                  ('Backdoor.Win32.PcClient.dfs', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '0216c876790974f58bfa97f39c75de40ff98531a93c4d9a4108bd19584b0834f'}),
                  ('Backdoor.Win32.KeyStart.v', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'ARBE', 'ARI', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ivm', {
        'actions': ['RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE',
                    'ARS', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                    'ARI', 'RS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fka', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARBE', 'RS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nuclear.fn', {
        'actions': ['RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARI', 'RS', 'RS', 'ARI', 'RS', 'RS', 'RS', 'RS', 'ARI',
                    'ARI'], 'evaded': True,
        'evaded_sha256': '3b5a16ac37a93ab2b47e1d1e7c44f242162a688f24c628d369a8fcbc3fadd199'}), (
                  'Backdoor.Win32.PcClient.rg', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Netbus.Ripper', {
        'actions': ['ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.dml', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '3ad0b752baa8d8aaee63026a0c59023ca45ca57bcc3af6c98b4cf450bf206494'}), (
                  'Backdoor.Win32.PcClient.ihm', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'RS', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARBE',
                                  'ARS', 'ARBE', 'ARBE', 'RS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
                      'evaded_sha256': '8baff77a4e7260d3967c7944a83777ba6ba7ca4d54e059ae13d2f3fcabb1b217'}), (
                  'Backdoor.Win32.IRCBot.pu', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dxv', {
        'actions': ['ARS', 'RS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'd42b0ff4b51fe42e66d44cff1cfd096a85b51dd61bf519cd330316738f89f518'}), (
                  'Backdoor.Win32.PcClient.agz',
                  {'actions': ['ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'RS', 'ARS'], 'evaded': True,
                   'evaded_sha256': '9d623c23a68423dee8d92b83d2b73ad2ba7d8bcdf738f58cc857756d36d4a575'}), (
                  'Backdoor.Win32.PcClient.pwp', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'e03bf3c7238d0bc5a347ef5be1945f58d783cbcca3245f15c5c75fb058fd8489'}),
                  ('Backdoor.Win32.PcClient.zkd', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'RS', 'ARI', 'ARBE', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '74e62dfc7a4832e72447260e60ad9d8abc4855265e4d1693a672da800262d4b2'}), (
                  'Backdoor.Win32.IRCBot.gki', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Nepoe.dp', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jwt', {
        'actions': ['ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.dhr',
                                                                     {'actions': ['ARS', 'ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'b42eb544a554199a0db687ef07c20bf9a9b3701e17c53f8354e37d45763955be'}),
                  ('Backdoor.Win32.PcClient.az', {
                      'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS'], 'evaded': True,
                      'evaded_sha256': '6a7816b0fc082fe48c09caec4fd35af474418814d794696408f89116c10a4ddc'}), (
                  'Backdoor.Win32.PcClient.cix', {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '39dfb21c8509071c9cb16ceecadf083c44f8ad163ee2622fda001d7a8f153124'}),
                  ('Backdoor.Win32.Nethief.XP.g', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.MSNMaker.ag', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARI', 'RS', 'ARBE', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.czr', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': 'f1eb35053f2552af6407c02e21df98ab419cd3e25ea22ad7bd8153b406c76f4c'}), (
                  'Backdoor.Win32.PcClient.gsw', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.cwb', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'RS',
                    'RS', 'ARS', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.LittleWitch.61.y', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fyf', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARBE', 'ARS', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.gay', {
        'actions': ['ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'RS', 'ARI', 'RS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.eks', {
        'actions': ['ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS'],
        'evaded': True, 'evaded_sha256': '0000b9a35c1b9a8d3f6ea276e85d8d8c6646cfd169ce48bf69623c38737c2480'}), (
                  'Backdoor.Win32.PcClient.axe', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'e8813e6f95e6dffad2170720bb0c58bdb4624f9ee7c02083d44a232b331a4b1d'}),
                  ('Backdoor.Win32.NetControl2.293', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE',
                                  'ARBE', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.avd', {
        'actions': ['ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.gia', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.NewRest.h', {
        'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'RS', 'ARI', 'ARI',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.mso', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '18a0a0bab8d260aebe367ca0eba42665c41b2b320d33ede39c1e0fdef9d4505b'}), (
                  'Backdoor.Win32.PcClient.esz', {'actions': ['ARI'], 'evaded': True,
                                                  'evaded_sha256': '2cda93cbe9f9199716a827e97e469790062418ac4f2b1bb2b832a29513bd3843'}),
                  ('Backdoor.Win32.IRCBot.hkh', {
                      'actions': ['ARI', 'RS', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS',
                                  'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bmg',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '7ccfbf8cf84e7602df7d6c9af64ec680d5d050af2e5b24d0d4d1abddc713c5e0'}),
                  ('Backdoor.Win32.PcClient.doc', {
                      'actions': ['RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI'], 'evaded': True,
                      'evaded_sha256': '4bc81ff9e8daa67e32a47f3452e9600ab2712536001726a7d1cc18d89ae09b0c'}), (
                  'Backdoor.Win32.PcClient.ewe', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI'],
                      'evaded': True,
                      'evaded_sha256': '2a807f6e43e8f0e43dbda65b32238ddeb730b3242579868636fb7ceae1853c5d'}), (
                  'Backdoor.Win32.PcClient.seq', {'actions': ['ARI'], 'evaded': True,
                                                  'evaded_sha256': 'db531367148ad4eb5dbc9eda7a58095eb8048610874c8be7bd6a2ea80798ce97'}),
                  ('Backdoor.Win32.IRCBot.ggf', {
                      'actions': ['ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Karakum.a', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.dte',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': '80e0696256a6a42d5d5d8046a7bba3698cb41e66b73d937fcc026b4c491b15bb'}),
                  ('Backdoor.Win32.PcClient.bpp', {
                      'actions': ['ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.lvw', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARS', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS',
                    'ARI', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS'], 'evaded': True,
        'evaded_sha256': '26e87b25fc1f04d61ea08e03b08c91209749f7dc6b929870ca510e1def31336e'}), (
                  'Backdoor.Win32.Masteseq.aj', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'RS',
                                  'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.chs', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': '04528b94a990a6eea40aa3585771713dd5e95b9fe5c8d1f8b561efa0d1d777c0'}),
                  ('Backdoor.Win32.InsultMedia', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.IniKill.32', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.dnx',
                                                                     {'actions': ['RS', 'ARI', 'ARI', 'ARS', 'ARS'],
                                                                      'evaded': True,
                                                                      'evaded_sha256': 'cba6b394301bbf58368aef82eea828ff473c74a33dbbbdbdcda661f317c27ba9'}),
                  ('Backdoor.Win32.Poison.czb', {'actions': ['ARS', 'ARS'], 'evaded': True,
                                                 'evaded_sha256': '96c94793162363d4569aeb13f3d7b3c61538ac8291d5759a8132a47782954937'}),
                  ('Backdoor.Win32.Latinus.c', {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                'evaded_sha256': 'f5b5f220ebf43ee7cf09334b3b7295ad58371fc1e79cec0a14a8d6218ea58530'}),
                  ('Backdoor.Win32.PcClient.eio', {
                      'actions': ['ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.drk', {
        'actions': ['RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARI',
                    'ARI', 'ARBE', 'ARI', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.NetTrash.10.b', {
        'actions': ['ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'ec3bd28a2e7c6ebc38b306b5c180bd671bc562ade92cfc06689806581a8a3000'}), (
                  'Backdoor.Win32.Nuclear.go', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '238a341aea4d761df27d4f2f8061d151a8711454a4b75fa158d92b461d4eed98'}), (
                  'Backdoor.Win32.PcClient.nck', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'fda46fa1b88aa14e7af576c007b80533f18841d494b140217baefab397879d12'}), (
                  'Backdoor.Win32.PcClient.cgw', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Poison.cyh', {
        'actions': ['ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS'],
        'evaded': True, 'evaded_sha256': '58a60c8b7511a6c62042e18a9c0f01e12d2c60003b4b9bb838fac95d7f854f8e'}), (
                  'Backdoor.Win32.PcClient.zks', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.MiniCommander.10.a',
                                          {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                           'evaded_sha256': '747715bd496a2d2352a880f67ac1cb18dc657b6b92b1f966e4c7adaa8d3b7dc4'}),
                  ('Backdoor.Win32.MSNMaker.cc', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ebl', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': '5a3a414c9fc4454126a30ebce3b1ca8e16aedbfbb0bd6e6b8bfe063265a31c9a'}),
                  ('Backdoor.Win32.PcClient.llx', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': 'bfaa4a574bcae1a20aea9dd3a34adb62caaffb7b82c1f8bcc6bc396b63e8324c'}),
                  ('Backdoor.Win32.Poison.bef', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.duc', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARS',
                    'ARS'], 'evaded': True,
        'evaded_sha256': '2c8699e7dac2a089541c690add1fdbece6843683941c72b5311dd6898ea62d4c'}), (
                  'Backdoor.Win32.MSNMaker.be', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'RS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.oen', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
        'evaded': True, 'evaded_sha256': 'eefb127a27b10d5c18caf01256ccb0b2e2c157d1cae0d7eac2711214992fca66'}), (
                  'Backdoor.Win32.PcClient.pkv', {
                      'actions': ['ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Nethief.15', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Litmus.108', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.gjm', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.en', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.dwz',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'be2fdb3f014340f7463387632d95993c2da384d22ccfa05754bbb536b7c62711'}),
                  ('Backdoor.Win32.PcClient.bcr', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '7d1de2281ea5c0913673cda9d6b777cf31004a642d58ccceba9fd96d29c905ac'}),
                  ('Backdoor.Win32.PcClient.ebt', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fco', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                    'ARS', 'RS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Padodor.am', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARS'],
        'evaded': True, 'evaded_sha256': 'fda50ebfe79cfb97725a994f32b52225dffa58f68c60ac0df3d29809614e9c4e'}), (
                  'Backdoor.Win32.IRCBot.grd',
                  {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                   'evaded_sha256': '06058d48cf0ba0d025a90fe1bcc10f2f0805e2963e856bda1f3a50c001f4fa51'}), (
                  'Backdoor.Win32.PcClient.ovb', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.qjd', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Poison.bkc', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': 'b927c409256bf67bb76ccfb7ca4919e97c9f9171dc7a3f108b97879fe11e218f'}), (
                  'Backdoor.Win32.PcClient.ajp', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'ab1fae1288aad7fca6e4a95d6d68a7bc93656e1bef6dbbf0af25d8173450233c'}),
                  ('Backdoor.Win32.PcClient.pxe', {
                      'actions': ['ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '199260983fe4ca6b1a9daea2e3bdcc8afad7aef8d4509cb5318229b835c608b7'}), (
                  'Backdoor.Win32.IRCBot.gjo', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.jdc', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.iqf', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'e0039966da5bc39bb3424516f1f7dc9508e08c8e944ec572c9706edf335b6400'}), (
                  'Backdoor.Win32.PcClient.amp', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.izo', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.egu', {
        'actions': ['ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '6740007ea77b05a4d6d8fe699b83d42da8e3c36ddb9683e4607837a783180dea'}), ('Backdoor.Win32.Jes.16',
                                                                                                {'actions': ['ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'RS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'RS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI',
                                                                                                             'ARI'],
                                                                                                 'evaded': False}), (
                  'Backdoor.Win32.PcClient.dmi', {
                      'actions': ['ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '7c6b7c5cfd9275ea5d9e556ba62cb41e586fa9eb96dc65674b44211c2893c396'}), (
                  'Backdoor.Win32.PcClient.uac', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'e6b461b06db3d2bdb0fa36a657052078063d8a62194e0400bbfced4c0156f8bd'}), (
                  'Backdoor.Win32.PcClient.agk', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Hupigon.zjm', {'actions': ['ARS', 'ARS'], 'evaded': True,
                                                                         'evaded_sha256': 'c0c932029355c4f655a72448d610c802ca18b803b55ed69d052ad5b3c224fcca'}),
                  ('Backdoor.Win32.Liondoor.k', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '66f1c4b5964cd5396b86938bb27011c7546b6da722dee7f1d0d151f6f6f38f02'}), (
                  'Backdoor.Win32.PcClient.cbl', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '9fef6dbf7f757d63aaba22cb62187954bfad17bd264bad3e5da38ee613d1f3e1'}),
                  ('Backdoor.Win32.PcClient.bf', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Poison.crn', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.MoSucker.20.b', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'a9694a01be03bae15aad08a4e112ba4b1133ea91663173b50951ea50f13f0b88'}), (
                  'Backdoor.Win32.PcClient.gat', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': True,
                      'evaded_sha256': 'd6351f51bdb7c44506104e7fd7783a2830dad2cdd19423b01fbfd2f78a1b50ad'}), (
                  'Backdoor.Win32.PcClient.svp', {'actions': ['ARI'], 'evaded': True,
                                                  'evaded_sha256': '59443925c56e7dbe4025b77376013612cb50b597f0a2360ee3230b97ed2c9fed'}),
                  ('Backdoor.Win32.IRCBot.ggy', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.oha', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.mw', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jea',
                                                                      {'actions': ['RS', 'ARS'], 'evaded': True,
                                                                       'evaded_sha256': 'ff75175d85df05ed0f34c6196e5ec267284d5f36508a5636547e327eb73e21fc'}),
                  ('Backdoor.Win32.PcClient.rbv', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Poison.dng', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.dai', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.hpa',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'afdc0317046c0a044351f83aaff003fc1936f88b38707404a20ca77d9f97a3fe'}),
                  ('Backdoor.Win32.Nuclear.tg', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.lyx', {
        'actions': ['ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.dgu', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARBE', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.bad', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.crq',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'e75b5cfeef59bc72e76627d73bbd2cedde6c7b5085c4296de3e5c8d6f6cec7af'}),
                  ('Backdoor.Win32.PcClient.bql',
                   {'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                    'evaded_sha256': 'e2368d277c54cdb61f9749599b81060d33a5da7e19a3363c0e771adab46561ee'}), (
                  'Backdoor.Win32.PcClient.cvv', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.y', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.lmg', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '5af70df6f235c71177587e759189792f1ec1a3333843f444970c8f85083823a6'}), (
                  'Backdoor.Win32.PcClient.ndn', {
                      'actions': ['ARI', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Poison.amr', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.mox', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS',
                    'RS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fro',
                                                       {'actions': ['ARS'], 'evaded': True,
                                                        'evaded_sha256': '47c223115d556183a61ca43e617b7045c840fe2ea09f3a91341dabf778011e93'}),
                  ('Backdoor.Win32.Loobot.a', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.oew', {
        'actions': ['ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'ARS', 'RS', 'RS', 'RS',
                    'ARBE', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI'],
        'evaded': False}), ('Backdoor.Win32.Iwanywhere.12', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
        'evaded': True, 'evaded_sha256': 'b9baf2786d54ae009b87571c86d3ca8af50bbe97fcc3d625318c1d0e4ce769a5'}), (
                  'Backdoor.Win32.LittleWitch.61.t', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '21814a687969778e53432e5904cab0a4cb37aaada8ffc006c6f2fa4fb4fd542f'}), (
                  'Backdoor.Win32.Nucleroot.aa', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.abs', {
        'actions': ['ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'RS', 'RS',
                    'ARS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.eue', {
        'actions': ['ARS', 'RS', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'ARBE', 'ARBE', 'ARS', 'RS', 'ARI', 'RS', 'RS', 'RS',
                    'RS', 'RS', 'RS', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nethief.49', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.ric', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Pahador.an', {
        'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.qxb', {
        'actions': ['RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.rbz',
                                                                     {'actions': ['ARS', 'ARI', 'ARI'], 'evaded': True,
                                                                      'evaded_sha256': '3d0775374954448fe2cc27be929f6e0017d1db9ee616c69ac1ed375edc9e3192'}),
                  ('Backdoor.Win32.PcClient.kin', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '2cb8807bab2497e663b4a065d9befb5cb7ae426a8a87e61565497bbc681c93fe'}), (
                  'Backdoor.Win32.KeyStart.o',
                  {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                   'evaded': True,
                   'evaded_sha256': '269be0e9c45561e1df0f4a7451f81d6fe2d4f2c72a136216d575a5382bc3b0d2'}), (
                  'Backdoor.Win32.MoSucker.ib', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bmu',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '94b6b17be19514c0d6304497020a18ae8852429541041c89a8f9d282119153e4'}),
                  ('Backdoor.Win32.PcClient.bkk', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'a37880d3fce935f1089bccc64cffa24d877b56c7b95d198af73ff7e238e782a2'}), (
                  'Backdoor.Win32.MoSucker.30.c',
                  {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                   'evaded': True,
                   'evaded_sha256': '0defe6b9acdafdaa4d9442efbf4d27b088a5172499d20adb2ded0aee4d748d63'}), (
                  'Backdoor.Win32.PcClient.mih', {'actions': ['ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': 'f8f8d492c5787f181fdab8fe430e9a353538a6341358def664582925eb46cc26'}),
                  ('Backdoor.Win32.IRCBot.i', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Pahador.aw', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.hqm', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.hxn', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '99590902428626a45b0f54ceeeb2ca2f8434b2cc031edf077d29b66994229a5a'}), (
                  'Backdoor.Win32.IRCBot.gwb', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.cmd', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': '13cf25434f11b2b4bc6ab1e0a9ba5d90aa50e40b1959ee3d053d0f9608af131f'}),
                  ('Backdoor.Win32.PcClient.pkf', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Jinmoze.1866', {
        'actions': ['RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.gvc', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '3636303b9da7ced7bca9c862575b8c1fcd5510f4821e578b1b6339f3e5307cea'}), (
                  'Backdoor.Win32.PcClient.bqv', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '75d60bf1aedd5e3da05812b171b6648eb66ba24a64adf76267e7942eac60a35b'}),
                  ('Backdoor.Win32.PcClient.elk', {'actions': ['ARI'], 'evaded': True,
                                                   'evaded_sha256': 'fc03f6876feebdfebdf0b830a64d3f56305d63148c39763bf36d750f32f3091e'}),
                  ('Backdoor.Win32.Padodor.au', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Nuclear.d', {
        'actions': ['RS', 'RS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.LittleWitch.501.d',
                                                                     {'actions': ['ARS', 'ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'd938055e4b6d747c28452f7ca1409602933acc1767e3bca06110447fe6f951a3'}),
                  ('Backdoor.Win32.PcClient.aboc', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.IRCBot.yy', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.eqs', {
        'actions': ['ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARI', 'ARS', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.bkv',
                                                                     {'actions': ['ARI'], 'evaded': True,
                                                                      'evaded_sha256': '4509c0d8f695918afb5b95999ee320384ca97ee2bfbf35c460b3ca2ad10e104a'}),
                  ('Backdoor.Win32.PcClient.ehm', {'actions': ['ARI'], 'evaded': True,
                                                   'evaded_sha256': 'df1316cc53521778aabab31c114fc5441ff72c31bc2f557dda17a82c5e736f2f'}),
                  ('Backdoor.Win32.Massaker.11.a', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARBE', 'ARBE', 'RS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.yny', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Opwin.11', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.JJB.10', {
        'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Inject.lh', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.gru', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS',
                    'RS', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.myy', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
        'evaded': True, 'evaded_sha256': '34ca5df47d584fdd76ae83834fee6cbba89d9dea559c17161014158ec6bb0fab'}), (
                  'Backdoor.Win32.Poison.avh', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Hupigon.zoa', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': 'f661686707c94db55fa0c7bbfea6571596abe653709980e5c6a2c7eac17f2878'}), (
                  'Backdoor.Win32.Kbot.en', {'actions': ['ARS'], 'evaded': True,
                                             'evaded_sha256': 'd35306234ca82d352a859b6d837869aeeecde6490225f7b67d119a378576cb0c'}),
                  ('Backdoor.Win32.PcClient.dlp', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'ARI', 'ARI', 'ARI',
                                  'ARI'], 'evaded': True,
                      'evaded_sha256': 'f22cfee46bffab88df7bd19b9abd84070f69922bc43e5fa0c14e43e7f12c15d6'}), (
                  'Backdoor.Win32.PcClient.fnj', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '42bda3406292450548646abb4ee987924aa145bdd1c6885283b5b1512350b9f0'}), (
                  'Backdoor.Win32.Joleee.f', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.NetShadow.i', {'actions': ['ARI'], 'evaded': True,
                                                                         'evaded_sha256': 'b018e3ed25af888f961c24309784c85dd3f4efe7f897fcc56f60250f46e39889'}),
                  ('Backdoor.Win32.LittleWitch.61.k', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS',
                                  'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': True,
                      'evaded_sha256': '4d903ad5e9755495673dc7a086299c6d287654d8e29bd3fa332af687c2f5bcce'}), (
                  'Backdoor.Win32.PcClient.jdd', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARBE', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARS', 'RS', 'RS', 'RS', 'RS', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.Optix.01', {
        'actions': ['RS', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
        'evaded': True, 'evaded_sha256': 'eed863704a01567204fe9681fa7c2aa31b540c050455540f036dbbc683f54d9b'}), (
                  'Backdoor.Win32.Iroffer.gj', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS'], 'evaded': True,
                      'evaded_sha256': '4f90015727686bac0ba53db8989592be7c6e15ddf6d63c6f034cdf525d6454a5'}), (
                  'Backdoor.Win32.PcClient.ajg', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '975fac72ce8b6f8309d06413a42a37e0a2d1c81e48a883e90936811a1932bec2'}),
                  ('Backdoor.Win32.Netbus.12', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Lithium.10', {
        'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.byx',
                                                                     {'actions': ['ARI', 'ARI', 'ARI', 'ARI'],
                                                                      'evaded': True,
                                                                      'evaded_sha256': '5c2cd6bc38b10b4117712c8997759c298b361206b011bb52415136e99e5ab17f'}),
                  ('Backdoor.Win32.PcClient.mws', {
                      'actions': ['ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': True,
                      'evaded_sha256': '8022adace9e8d83228ff9508a0abfd51b93c7574a22e9ac74b2d81cc02b065e7'}), (
                  'Backdoor.Win32.KheSanh.210', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dpi', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nuclear.ct',
                                                                     {'actions': ['ARI'], 'evaded': True,
                                                                      'evaded_sha256': 'c92de717dda1cc9296fab7305689ed203e54a76e8e3b7208341bf6fca3d72cd7'}),
                  ('Backdoor.Win32.Poison.bkj', {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                 'evaded_sha256': 'c9953e165adc5fc29ebcaa95cf7c0debccc15bf46b230532df6d5de511eeea15'}),
                  ('Backdoor.Win32.Pahador.t', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'ca399d3ae251b2b843fcd4164d0ace427c9035a92572a94912d232b0c5f29b3c'}), (
                  'Backdoor.Win32.PcClient.qb', {'actions': ['ARS'], 'evaded': True,
                                                 'evaded_sha256': '8b970d0fee23f90240e11e1e49c2d48e86eeaf5a28c281dbd8d8cbda1c039d16'}),
                  ('Backdoor.Win32.PcClient.hfs', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Poison.dap', {'actions': ['ARI'], 'evaded': True,
                                                                        'evaded_sha256': 'a31216621961abd19296585f8aaa8cd3f755c61ae60f41e867153bba08befeaa'}),
                  ('Backdoor.Win32.PcClient.evu', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '9bc28b9160cf73be2af25e88e7d36ce665373f2d54ef2fb05cfdd7c586d55237'}), (
                  'Backdoor.Win32.Optix.Pager.20', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '1826fc03dc88052f06feef2eeaee370753702ac91732cf526d5592ce79730449'}), (
                  'Backdoor.Win32.PcClient.dlj', {'actions': ['ARS', 'ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '3dc571f7e45bad9cfb6ce58701b58a0503d5483bb3ba42f274bb13865cc35767'}),
                  ('Backdoor.Win32.Optix.tpjn', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.qkn', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
        'evaded': True, 'evaded_sha256': '897288decc4d314411a46d81f84275bff95d133014a703fd89d30357ce9169a2'}), (
                  'Backdoor.Win32.Mytobor.ag', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Inject.gn', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI'], 'evaded': True,
        'evaded_sha256': '49c0433168c37e6cb22397b2af5671698a5a12ba5162de8aed01a7ab1ba55cc2'}), (
                  'Backdoor.Win32.Nepoe.eu', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dom',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'RS', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '306e6fa3394e5101f4d068fdce15b7e360e5c9267060b124d830ea6e0fe6e788'}),
                  ('Backdoor.Win32.PcClient.fgg', {'actions': ['ARI'], 'evaded': True,
                                                   'evaded_sha256': 'fe56a3111e71acca11e3182198aa8c25f6d03f03f582a346d7886a45637cf2b5'}),
                  ('Backdoor.Win32.PcClient.hov', {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                   'evaded_sha256': '51fec0000dd80fc29023c89695f3f84b4253118bb5cae6b4ec1712c04a5c9f38'}),
                  ('Backdoor.Win32.PcClient.mbx', {
                      'actions': ['ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'eaba76f9c85d4b3c1e5fc14fc69d26a7673999dd51d2bd669966df0ab0b17b93'}), (
                  'Backdoor.Win32.LittleWitch.501.a', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'e11430540ea6789cfe07812a013930203107759cacbc7648c0f379ec509bca5e'}), (
                  'Backdoor.Win32.PcClient.gya', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'b6310f9da5fd78d29eef9eeededf5ea82551fd9dfb056ed1f6730c0e952caeef'}), (
                  'Backdoor.Win32.PcClient.nhd', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ofx', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
        'evaded': True, 'evaded_sha256': '430983c6b35098dce117c0027b170f0a73b37ee8dc5c897bf6862fcfe7fb6c94'}), (
                  'Backdoor.Win32.PcClient.jab',
                  {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'RS', 'ARI'], 'evaded': True,
                   'evaded_sha256': 'b0728fbe84c54c33f0700788b5a8a62f43e13cc896b22b2041d7c71dffc6d1e1'}), (
                  'Backdoor.Win32.Kbot.eh', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'be4260f13bb1117a4af3157a9048fd332c9a0e3ddc78a6bd92c003b5e55e8cf9'}), (
                  'Backdoor.Win32.PcClient.hih', {
                      'actions': ['ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS',
                                  'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS'], 'evaded': False}),
                  ('Backdoor.Win32.PcClient.ixk', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ftn',
                                          {'actions': ['RS', 'RS', 'RS', 'ARS'], 'evaded': True,
                                           'evaded_sha256': '1b290ce32693ef377ff65d861c8fed3de27b0c282573ac921a7b0895ad6f1845'}),
                  ('Backdoor.Win32.PcClient.dqd', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'a910ccd87da11453e0128044838e04612baa034f3c1ec751606b1c204c28143e'}), (
                  'Backdoor.Win32.PcClient.pjz', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '155ef19daa07634b16e180d59029d66d3b81d634035f1b93d034eb780714e917'}),
                  ('Backdoor.Win32.Kbot.eb', {
                      'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'b859e2b3a2579f83ca8830d99599769485251b557d7d916eab42f7e9e60efe78'}), (
                  'Backdoor.Win32.LittleWitch.41', {'actions': ['ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                    'evaded_sha256': '952cd3f9ab30474963ba0b12db1f032b222a0e15d035750e25ef53f271ae3f1f'}),
                  ('Backdoor.Win32.PcClient.fiu', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Nuclear.ax', {'actions': ['ARS', 'ARI'], 'evaded': True,
                                                                        'evaded_sha256': '71d7128d33d30a4d294dae42c89b74b123ae0eec05c0d9580d128998ad9cce5f'}),
                  ('Backdoor.Win32.PcClient.frg', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'RS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.hoq',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '36118563b0d3ebea5012685f22ffc8b0b48a3785ae50aecfe608427a9f1d1855'}),
                  ('Backdoor.Win32.PcClient.foi', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '60e8e02e3f284c2a5703a57a879d72ab6a9e80e52e206c01cbef467b4aa9242a'}), (
                  'Backdoor.Win32.Ltools.e', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.eku', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'RS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Pakes.a', {
        'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'RS', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.pfk',
                                                                    {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                                     'evaded_sha256': '5e1ba4781bde24315a1b672de452a171b0d743f87aba677d04038077c287724f'}),
                  ('Backdoor.Win32.PcClient.auk', {'actions': ['ARBE', 'ARS'], 'evaded': True,
                                                   'evaded_sha256': '82a1b3e6563b671d7d28e4ad6db507996182ecf845f9ac5a9bfa5b93739297be'}),
                  ('Backdoor.Win32.InCommander.16.b', {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                       'evaded_sha256': '8ef3d37e9643f8c8a22033f5082bbd98e9af8adc1cbd4f59504b67805a275ac3'}),
                  ('Backdoor.Win32.PcClient.hwq', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': 'dde09b89845e1a64e57e1781a25405eaf644e670fda7d18ed3c16053a1c395d2'}),
                  ('Backdoor.Win32.IRCBot.sj', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.exu', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI'],
        'evaded': True, 'evaded_sha256': '6776c0de8113efc45274cb336ab359bcc5ca809f11c8f449fff99403e3fecee7'}), (
                  'Backdoor.Win32.PcClient.ceo', {'actions': ['ARI'], 'evaded': True,
                                                  'evaded_sha256': '16b139d434d4b353654e94738a60e237169bee94a3d0d987b4e8f76f4e3c3214'}),
                  ('Backdoor.Win32.Poison.acyn', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '256dff5a62b45f26c2c477a2b80f2354494ce6d716346a93583263d5ab820f39'}),
                  ('Backdoor.Win32.PcClient.npy', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'e390c0d7e4dc2ea4f92d2d8601410bcc90e9ee655deb529d53a8eec989cc4cf8'}), (
                  'Backdoor.Win32.PcClient.flh', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.lib', {
        'actions': ['ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.ojm', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.fdg', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '5d17dff39de6ad3a53e3623904b4b6abaddcde631065b21f3ce3cc2460a03923'}), (
                  'Backdoor.Win32.PcClient.cbe', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.MMX',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                           'evaded_sha256': 'ff25f181926eb3619ac5cd45839cdde9d81426d8b7d6dd4e7f79032664797a4b'}),
                  ('Backdoor.Win32.Kbot.qd', {
                      'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.hsi', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARBE',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.fjm', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '9358a0ac5331cc748ede97ce7f8955b34fc3e7e7ae94c9c3422b3c41bfc1b39d'}), (
                  'Backdoor.Win32.Netsnake.bg', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.abeu', {'actions': ['ARI'], 'evaded': True,
                                                                           'evaded_sha256': '6703d791e6f390933b5d354d353efc00cc5bb9e63443cc0447f3e733d300cc19'}),
                  ('Backdoor.Win32.PcClient.dno', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.pcy', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'RS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.IRCBot.hbx', {
        'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.edi',
                                                                     {'actions': ['ARI', 'ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'edcdd05c4900b83bb34bb06b7e9bee9abec5416e036b164953e24a305aa0b216'}),
                  ('Backdoor.Win32.PcClient.kmi', {'actions': ['ARI', 'RS', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                   'evaded_sha256': '255ee22f168bc1509a4a2bbefd291131bbb8b9bcb50f3d394b58988ca5d7e64a'}),
                  ('Backdoor.Win32.Nucleroot.w',
                   {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                    'evaded_sha256': '8c4b91ba6e2a4d57871074ed0353c8113c9d08795ea78e099200da62ba87dbcf'}), (
                  'Backdoor.Win32.Outbreak.100.ah', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '234d9e91f2c7778e58ebf3a65626342fc86dfc15ed49b77a1e2b2cce9cb132a5'}), (
                  'Backdoor.Win32.Pakes', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': True,
                      'evaded_sha256': '0174b953d1f96b9567d7140651ce6ab14f6c8e2b26ec664007cc499b418312ea'}), (
                  'Backdoor.Win32.PcClient.med', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Optix.Pro.z', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'bb2d8c7c2d681571919e97be1fd953b692f0596ba7f0bbc8652c062f953405a9'}), (
                  'Backdoor.Win32.PcClient.rul', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.acv', {'actions': ['ARI'], 'evaded': True,
                                                                          'evaded_sha256': '308db71f4e83ffcddd1f86307e90d00a98f5280ffa889d13fe6c73f6af4468df'}),
                  ('Backdoor.Win32.MiniCommander.11', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '39ceef3fd65e3c0ac63011f959c8cb21860f44fbe6a7bb0d518adc69dc77f6df'}), (
                  'Backdoor.Win32.PcClient.ida', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.akt',
                                          {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '516a76e542795528a22b7b453ba8e81c3a7e7f0842be66e638ee7567279f2d80'}),
                  ('Backdoor.Win32.Optix.Pro.f', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ghd', {
        'actions': ['ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                    'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'fcd6603ea03bc8788687b71759435e79c668711c172cbc9e27738ea5d8885145'}), (
                  'Backdoor.Win32.PcClient.cyq', {'actions': ['ARI'], 'evaded': True,
                                                  'evaded_sha256': '2214a15f4edf5fc1178deb39e0a7a73879518e5c916a6c3fcf4898c744d9fad1'}),
                  ('Backdoor.Win32.PcClient.css', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.lwh', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.xn', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS'], 'evaded': True,
        'evaded_sha256': '377587923969184fb7dce5e7f3c461842645cc9abc7aabd638a1dde94ad045c8'}), (
                  'Backdoor.Win32.PcClient.atu', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'b9c0278360dce2ec8e5458e50db9ffd2fb417c0f203122c7c27a8015ca56ff3a'}),
                  ('Backdoor.Win32.Litmus.002', {
                      'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.gfv', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '8f16ecb4bf04da0056bdf577ffc332ef4ca2d17380ead3f5fd1dd7cd92c5673a'}), (
                  'Backdoor.Win32.PcClient.gzd',
                  {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS'], 'evaded': True,
                   'evaded_sha256': 'f02d3b6cc842a7daff3ac3bbc7c28e4f762164643bd1cdd60a3f85ca95c3b8c3'}), (
                  'Backdoor.Win32.PcClient.ajo', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'c333a27094c68a5a7393673dd8fc30d08dc24dea40ec1bfc745554c7eaa49e89'}),
                  ('Backdoor.Win32.PcClient.mji', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Hupigon.zay', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Poison.alha',
                                                                     {'actions': ['ARS', 'ARS', 'ARS'], 'evaded': True,
                                                                      'evaded_sha256': 'dfce50116daea2ec2a7510b47abcd3c98b348ac498fc9ab60e6f4fbd9a4d89d0'}),
                  ('Backdoor.Win32.PcClient.gyi', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '5018032c498955e99f723d742c8804f436f81ab967d9e10e1b005e36d890e525'}),
                  ('Backdoor.Win32.PcClient.asd', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': 'c9c9364c49977137c6b124230c6be4c528a31b7544dd988def26372817e1fe44'}),
                  ('Backdoor.Win32.Hupigon.zfs', {
                      'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ouz', {
        'actions': ['ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '2dfafd8e894583eff003e54828b2b5c0a6aa81f32cb8bc8c277473ff287c6e10'}), (
                  'Backdoor.Win32.PcClient.cfy', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': True,
                      'evaded_sha256': 'ba268678d085e5cc2861414faba1316b849e78f33f9755da61d9b8b6818ab873'}), (
                  'Backdoor.Win32.PcClient.brp',
                  {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS'], 'evaded': True,
                   'evaded_sha256': '0dc63469c0acc9bd0aa90284582a64aa07096f840e916baa210ea8b63860675b'}), (
                  'Backdoor.Win32.IRCBot.hrx', {
                      'actions': ['ARS', 'ARBE', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.IRCBot.hcb', {'actions': ['ARS'], 'evaded': True,
                                                                        'evaded_sha256': 'c93705a4b5eef2ef39a4485a0e810cb761fc54da64eea5335a728e2560cd8246'}),
                  ('Backdoor.Win32.PcClient.fwf', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '628b5b3af515cfa47165200d7979e713598b019e0d21a31b0217366e1947721f'}), (
                  'Backdoor.Win32.PcClient.lrr', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Nightcreature.a', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '2745d9928db5925b2d9a5005c1ff3af16a496c381629d0ab6323829de4c321b9'}), (
                  'Backdoor.Win32.PcClient.cut', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '977f183e03111e67e53e74efb5be1bd55bc6ce12425552290da8ef2547757151'}), (
                  'Backdoor.Win32.PcClient.azk', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '60a51c48d7c8999846c49f12052af9f3e3bd81746780455c7af36bc02496e561'}),
                  ('Backdoor.Win32.PcClient.ff', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.ldw', {'actions': ['ARI'], 'evaded': True,
                                                                          'evaded_sha256': '18a2e7366fd3a4c9dafcee498b243aee47cecfd09cf349d2effbffb112055d61'}),
                  ('Backdoor.Win32.PcClient.aane', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Mydons.b', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '5daa4e23ca4f49d5110b5b168c08c670f11bf8fa5127be98608fa23cc50c37ec'}), (
                  'Backdoor.Win32.PcClient.ezi', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '61610a94288db15e0d9285f329bf65cd8801e0751ee4faf55b778813bc7fedb2'}),
                  ('Backdoor.Win32.PcClient.iwb', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.oem', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': 'db6b347dc97d6c61d96be934cf37327f7b59e528f54494b108c73115df8e7da5'}), (
                  'Backdoor.Win32.PcClient.mmc', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.szt', {
        'actions': ['ARS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.bjd',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': '9518a8363dac631a645bba5cdd5b3c283bb723d3a94263550d697a8d2c3b5c3f'}),
                  ('Backdoor.Win32.PcClient.eyo', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.oj', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.kav', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'RS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.lsk', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.jvs', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.dkh', {
        'actions': ['ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '5a2cf6cb25996be28128c2950f0410d2cc7ad49b9c78faccf0b04ebe7528b9d8'}), (
                  'Backdoor.Win32.PcClient.alj', {'actions': ['ARI', 'ARI', 'ARBE', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': '9b301c6a30899f037ec288adbe5a88adfa136d874a867a5c64fcd9a618decf5f'}),
                  ('Backdoor.Win32.IRCBot.rk', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Optix.Pro.i', {'actions': ['ARI'], 'evaded': True,
                                                                         'evaded_sha256': 'b4bb948af8178a829f4470a89f3b912a653453371efd0b11fffef4fbfd6bb330'}),
                  ('Backdoor.Win32.Nuclear.bg', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'a80cc0214fd0d4ff8616813038c6997d5c2246d4553c352130a100fe1cab094c'}), (
                  'Backdoor.Win32.Pilon', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARBE', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Pahador.ao', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARS', 'RS'], 'evaded': False}), ('Backdoor.Win32.PcClient.clt',
                                                                    {'actions': ['ARI'], 'evaded': True,
                                                                     'evaded_sha256': '7b5ed2af620a88820e50d5663413d0630cf3d76b667716e3182293262b1148da'}),
                  ('Backdoor.Win32.PcClient.mhm',
                   {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                    'evaded_sha256': 'f3b7caccb9c71c459ffcadf51df5e8c5cdbea0a737e125517c67c148cd53cd5a'}), (
                  'Backdoor.Win32.Optix.04.d', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.acc', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '12f198f545cebcf2809a715ef5aa1e16639aa92b06a540b2f3bdb8aa3925b13d'}), (
                  'Backdoor.Win32.Nuclear.sr', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARI', 'RS', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.amb', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': 'b618ce06530cb406adf5afffffcf8b01b53adb917809a537c9a6d5ee1d527db4'}), (
                  'Backdoor.Win32.IRCBot.hrw', {
                      'actions': ['RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARS', 'RS', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.elv', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Nepoe.d', {
        'actions': ['ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'RS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.chw', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'ce27f3a9c0a438f83d9c1a7929d80c6cc34d9de4a66865d672263ac735c9dec2'}), ('Backdoor.Win32.Orion',
                                                                                                {'actions': ['ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'RS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARI',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARS',
                                                                                                             'ARBE',
                                                                                                             'ARS',
                                                                                                             'ARS'],
                                                                                                 'evaded': False}), (
                  'Backdoor.Win32.PcClient.dsn', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARI', 'ARI', 'RS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.ent', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'e2844309a8948a34489267375f33c5602a9f4544fa39c6797bcf81400b52849c'}), (
                  'Backdoor.Win32.PcClient.bwa', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.bka', {
        'actions': ['ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fja', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '817edcfd40538db9cb66a857ec155bc5d0cd5356478dcf79a21bd8d5b0698c55'}), (
                  'Backdoor.Win32.PcClient.cko', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'baccfbdd5360349f9b07130defd9cd01e83f164943f667589fb49dfcb39e2ad0'}), (
                  'Backdoor.Win32.IRCBot.xz', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'b20405d8b0c2d7f92a6328a1f6046c06700103155e40dd7080423c18bc3abd41'}), (
                  'Backdoor.Win32.KeyStart.c', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.yqc', {'actions': ['ARI'], 'evaded': True,
                                                                          'evaded_sha256': 'aa7c8ff3f4ff2ab76953635a4cdec651d1d1b0ed0663fc920605fb6d8ddafe67'}),
                  ('Backdoor.Win32.IRCBot.ke', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fvd',
                                          {'actions': ['ARI', 'ARBE', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                           'evaded_sha256': '8eed05280bf7b018f914f7f299fde40c2775711c7e2a493677af0247e34dd1dc'}),
                  ('Backdoor.Win32.PcClient.zc', {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': 'a3f44b57664001c1a9d3dfe4467c948cebb58b01f0a57d2a8cc4cd3b3ad4a5b2'}),
                  ('Backdoor.Win32.PcClient.peq', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.MainLine.15', {
        'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE',
                    'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Inject.dg', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
        'evaded': True, 'evaded_sha256': '0791f0255ac2b55d3a2265b4ebdb2b8733e1136290155162806bd42c98193102'}), (
                  'Backdoor.Win32.PcClient.pki', {'actions': ['RS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': '8e91bc0d454eb90d877facd14cbbf6becbbb6954a6011808238b94b06e94c698'}),
                  ('Backdoor.Win32.PcClient.dph', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '568ab06e32bae8e85feb81c790c82ac3c9f75017449d54334a37d071769b9394'}),
                  ('Backdoor.Win32.PcClient.eol', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fhq',
                                          {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARS'],
                                           'evaded': True,
                                           'evaded_sha256': '4e469777f690bfeaae246cabdd5d649602534ef564be0843dd48b863d5d555f6'}),
                  ('Backdoor.Win32.PcClient.asj', {'actions': ['ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS'], 'evaded': True,
                                                   'evaded_sha256': '1766da74887a04439df73200f2b2181a3475a966d8b95b57da8d8b1e2cfbe60c'}),
                  ('Backdoor.Win32.PcClient.imm', {
                      'actions': ['ARS', 'RS', 'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'RS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'cf8f23f83f703f84ddc1cf7b1c79b6c44f544462e7491f0d297681a2cbcfd839'}), (
                  'Backdoor.Win32.IRCBot.gsf', {
                      'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.iin',
                                          {'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                           'evaded_sha256': '802b2a78c878d8a0003cf7bcbcaa65ea2484160ed662d22f3fea5e0bff11531e'}),
                  ('Backdoor.Win32.PcClient.fkh', {
                      'actions': ['RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.fax', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'd116038b1732abeac6509fca42bea81c7a3c76d3f5991497d621bfd470428f74'}), (
                  'Backdoor.Win32.PcClient.mii', {'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': 'cacae51b07430b8afdb18d5cf38a2527c4da0de9b51b2d0bcfa6ba19dde27ebe'}),
                  ('Backdoor.Win32.PcClient.rus', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Nethief.104', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.cjc',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': '2896fbbf97cd4ae6870a1e5ce06954005b94c0f33005f0000b82298d099eec50'}),
                  ('Backdoor.Win32.IRCBot.hza', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE'], 'evaded': False}), ('Backdoor.Win32.LanFiltrator.10.b', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS'],
        'evaded': True, 'evaded_sha256': '4d57306b4bb83c1188611ec8d0fbfca4ef24dea0f33b6af2e4638bae7a1715a3'}), (
                  'Backdoor.Win32.Netsnake.h',
                  {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                   'evaded_sha256': '71cb03f7f6fe2e591d7a197963b648afd0b2347692770ffbff2be05743af84a3'}), (
                  'Backdoor.Win32.IRCBot.zx', {'actions': ['ARS'], 'evaded': True,
                                               'evaded_sha256': 'd72e2495d77bd7603378b21d4bf6738ef7c0b34924d13985b2623d19c95ee7b8'}),
                  ('Backdoor.Win32.Poison.bbw', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.hxc', {
        'actions': ['ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS'],
        'evaded': True, 'evaded_sha256': 'ec3979d84346c87b50de18a17aaab7ea43f409f7342840ec74ed03e1034c9e06'}), (
                  'Backdoor.Win32.PcClient.cga', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': 'c02f0a208305b6be4b4f82de442ea6b0e20bc90a6118773cace94de744e75942'}),
                  ('Backdoor.Win32.PcClient.czg', {'actions': ['ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                   'evaded_sha256': 'bf0fbc4775107d745c00207d507569240417702a7b85c2c65976ba3e967ddcbb'}),
                  ('Backdoor.Win32.PcClient.pya', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '9775dd5ad8af2e7e43a17d17a0f1b0bd82277fa3e0d036bb9f4d5d377638ce54'}),
                  ('Backdoor.Win32.PcClient.jck', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.max', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IRCBot.hsv', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.aiu', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '5b763170327d007403cf4ce3142679fefa4a88e25ab268f779d537fe5807a39a'}), (
                  'Backdoor.Win32.IRCBot.xo', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Litmus.II', {'actions': ['ARS'], 'evaded': True,
                                                                       'evaded_sha256': '62a00b2a787236b81d0da63df6cb26a50c39b171ec83fa34b467570cb40f616f'}),
                  ('Backdoor.Win32.PcClient.lxb', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI'], 'evaded': False}), (
                  'Backdoor.Win32.PcClient.kn', {'actions': ['ARS', 'ARS', 'ARS'], 'evaded': True,
                                                 'evaded_sha256': 'cb2e32d4e219e467a4881568f7b9389fcc65444bc4bab75d4831935eafc2554c'}),
                  ('Backdoor.Win32.PcClient.ba', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '04fb45ab3cd54962aeb91a260990039775043775664154a3e3ed7ed4327e75eb'}),
                  ('Backdoor.Win32.PcClient.gnx', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': True,
                      'evaded_sha256': '2aea13d04a86651b9a81a548cc05dfaa4834d8596c78a50914c639f44c922261'}), (
                  'Backdoor.Win32.Officer.a', {'actions': ['ARI', 'ARI', 'ARI'], 'evaded': True,
                                               'evaded_sha256': 'a3fc4d7f0f7871844714404bd97a35c69af65e320e5a166d9a4f88e4b2a8476a'}),
                  ('Backdoor.Win32.PcClient.mvt', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': True,
                      'evaded_sha256': 'a146d0baa09db50ec4a2f9becef08be5eca9f0e45d8d7f770148d870e1131606'}), (
                  'Backdoor.Win32.PcClient.kbu', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '4a6daa6b13694ddeb4d9a4e4b25a6defbdf6c14e27d2bbac4df5278a937f2177'}),
                  ('Backdoor.Win32.PcClient.hva', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '584bb2b7eb28821ddb185d10e4c6464de036179ffeb6c047cb30d1a6d4e420f4'}), (
                  'Backdoor.Win32.Poison.bsh', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARS', 'RS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Pangus.m', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': '75fa9b65bd2883ab077e0b5548b16573d0897a4439856fa8c9b9c004b1bc3344'}), (
                  'Backdoor.Win32.PcClient.ugf', {
                      'actions': ['ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'f9479011213edf9d10675dab253d037f511f70441bb873ad62fb179851cab986'}), (
                  'Backdoor.Win32.Nethief.37', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Optix.tosm', {
        'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Padodor.bc',
                                                                    {'actions': ['ARS', 'ARS', 'ARS'], 'evaded': True,
                                                                     'evaded_sha256': '45ed8eef09916ea5f6bfadd16f26f8e7566d25001e8c686b6e45e89386bb2157'}),
                  ('Backdoor.Win32.PcClient.cac', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '1b679be877b9719f97b7292de13479c39afa0a0aea36e3ddddd2bd66a48e848e'}),
                  ('Backdoor.Win32.IRCBot.gtv', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Papi.q', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.cbq',
                                                                     {'actions': ['ARS'], 'evaded': True,
                                                                      'evaded_sha256': '09c4e5f5594d5529b0e8a1224c629859d816eb13085f12e3056280df5b9221aa'}),
                  ('Backdoor.Win32.PcClient.efy', {'actions': ['ARS'], 'evaded': True,
                                                   'evaded_sha256': '57525cf631c0908bd01442cedab598cbf9999bc50ddb2d4bb797a0ede38d879c'}),
                  ('Backdoor.Win32.Lecna.bf', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fou', {
        'actions': ['ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARI',
                    'RS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.poz', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARS', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.IEbooot.aq', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.MSNMaker.l', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': False}), ('Backdoor.Win32.Inject.dc', {
        'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARI', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), (
                  'Backdoor.Win32.PcClient.fae', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': '89b19c63f02376f014ee0c122bdd21c3ddcf6fc6e61d85e4c0e4275ab00bafba'}), (
                  'Backdoor.Win32.IRCBot.zw', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Nethief.bx', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS',
                    'ARBE', 'RS', 'RS'], 'evaded': False}), ('Backdoor.Win32.Lecna.i', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': True,
        'evaded_sha256': '76f5b10edf5d800debddadb14b295b59f5fbcb745f59f30f16e0a45314d48f59'}), (
                  'Backdoor.Win32.PcClient.loa', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'RS', 'ARBE', 'ARS',
                                  'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.lwa', {
        'actions': ['ARBE', 'ARS', 'RS', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'RS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS'], 'evaded': False}), ('Backdoor.Win32.PcClient.lqb',
                                                                                          {'actions': ['ARS', 'ARS'],
                                                                                           'evaded': True,
                                                                                           'evaded_sha256': 'b46d8a61db6d4baaa624c77731c6408d8e190a19a1eb8d50e168aebdda66fe2a'}),
                  ('Backdoor.Win32.IRCBot.gue', {
                      'actions': ['ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.fbc', {
        'actions': ['ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '1f98b8b58307d8e29693c5c697b3b8816285fda3dfe7c38058e92ec5693ca04c'}), (
                  'Backdoor.Win32.NoNeed.b', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.eia',
                                                                               {'actions': ['ARBE', 'ARI'],
                                                                                'evaded': True,
                                                                                'evaded_sha256': '80a6e6492e54e37750a5ef9c2eeb8199a811a8e015654c9661c726587a599334'}),
                  ('Backdoor.Win32.PcClient.dwp', {'actions': ['ARI', 'ARS', 'ARS', 'ARS', 'ARI'], 'evaded': True,
                                                   'evaded_sha256': 'aeb6986e674a51af013a8e1422cd1d2a7410643c317d3df26c5094e85b8d728e'}),
                  ('Backdoor.Win32.PcClient.besx', {'actions': ['ARI', 'ARI', 'ARI'], 'evaded': True,
                                                    'evaded_sha256': '042455d691cda47bb2de2dc082360aed164b2624f88e443eb7902263b05965f0'}),
                  ('Backdoor.Win32.PcClient.juf', {
                      'actions': ['RS', 'ARI', 'RS', 'ARI', 'ARS', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARI', 'ARBE', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Nepoe.n', {
        'actions': ['ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI'], 'evaded': False}), (
                  'Backdoor.Win32.PcClient.ddg',
                  {'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                   'evaded': True,
                   'evaded_sha256': '25271384f17981f3b3ba8a12fd26f5e5d6284fc6e09b9e59e053d48e38af98d2'}), (
                  'Backdoor.Win32.PcClient.fac', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '12b235349603caea6923627ef6b249a8e7a84b52b615965668ad1ae0454083a3'}), (
                  'Backdoor.Win32.PcClient.gbo', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'RS', 'ARBE', 'ARBE',
                                  'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.Netso.a',
                                                                                               {'actions': ['ARBE',
                                                                                                            'ARBE',
                                                                                                            'ARBE',
                                                                                                            'ARBE',
                                                                                                            'ARBE',
                                                                                                            'ARBE',
                                                                                                            'ARBE',
                                                                                                            'RS', 'RS',
                                                                                                            'ARI',
                                                                                                            'ARBE',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARBE',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS',
                                                                                                            'ARS'],
                                                                                                'evaded': True,
                                                                                                'evaded_sha256': '7a9a997251e58d05b010f6c217e365d34ddb580e28cb07a296dbe99e4cb2e36f'}),
                  ('Backdoor.Win32.PcClient.am', {'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': 'dcf78fd4cd778d84b0e2f44a4bf9930f0a92cdbfda01501d66b4e4158c13b1ac'}),
                  ('Backdoor.Win32.PcClient.gff', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARS', 'ARBE', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                      'evaded_sha256': 'a008be428e2929ba16b644f5e169f152b56fe480c673377f3d8051c5f8201158'}), (
                  'Backdoor.Win32.PcClient.sgc', {'actions': ['ARI', 'ARS', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': '62cd6ff1c7ccc1a6cfd67ffb501f02157548215792061df64201e1dbdf88ffec'}),
                  ('Backdoor.Win32.PcClient.bof', {'actions': ['ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
                                                   'evaded_sha256': '3ca61b50d313f685632eceb27950bf58c0198dc29ae9160494168e74745405f8'}),
                  ('Backdoor.Win32.Nuclear.bc', {
                      'actions': ['ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'RS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'RS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': True,
                      'evaded_sha256': '1f1854ef097d20359c36f4354343258d2cd16eefa5a1eb46da0392d561d80b88'}), (
                  'Backdoor.Win32.PcClient.kfb', {'actions': ['ARS', 'ARS'], 'evaded': True,
                                                  'evaded_sha256': 'cec806278e76c87b71220cc0b1375a43b1d5eee4183e7cf625893ddc2fe95fd5'}),
                  ('Backdoor.Win32.Nepoe.em', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dds', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                    'ARI', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '797114cd6e85772193f347a8dabf34ad0a43e3d6ea2e43fe8e19aba69b05a9dc'}), (
                  'Backdoor.Win32.PcClient.fad', {
                      'actions': ['ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARBE', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARS', 'ARBE', 'ARBE', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI'], 'evaded': False}), ('Backdoor.Win32.LanFiltrator.05', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                    'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE',
                    'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARBE'], 'evaded': False}), ('Backdoor.Win32.PcClient.fij',
                                                                                         {'actions': ['ARBE', 'ARBE',
                                                                                                      'ARBE', 'ARBE',
                                                                                                      'ARBE', 'ARBE',
                                                                                                      'ARS', 'ARS',
                                                                                                      'ARS', 'ARS',
                                                                                                      'ARS'],
                                                                                          'evaded': True,
                                                                                          'evaded_sha256': '870e13cf5ef425521ec8f8a05b2ebd7069d87b18101b17f962ff7653fddc2fda'}),
                  ('Backdoor.Win32.IRCBot.tq', {
                      'actions': ['ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.jtz', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'e4e368e2a36156c907375b068ac49d88cf1689ccea0eb0bc0e2340e996592f7b'}),
                  ('Backdoor.Win32.Optix.Pro.cj', {
                      'actions': ['ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '38f236e044dc87e9f6f886004f96a6a09a99036b282bc69d57153f840826609e'}), (
                  'Backdoor.Win32.Lamebot.a', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.dlw', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'c6ee403455eedef04f17855a8e5fc62bde3d6615c3134db66623b6fb02cb4bf3'}),
                  ('Backdoor.Win32.Poison.bsl', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS',
                                  'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.clr', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': True,
        'evaded_sha256': 'b937f8a01d92c3b481ad35e5edbf5b29822f1828471e40eda70affa3c3974396'}), (
                  'Backdoor.Win32.PcClient.cnv', {'actions': ['ARS', 'ARS', 'ARI'], 'evaded': True,
                                                  'evaded_sha256': 'aaa97c4a61bee65b643724c18c44e26291bf8da8f3b5e24f05b2b2395568c7e1'}),
                  ('Backdoor.Win32.Poison.dpw', {
                      'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS'], 'evaded': True,
                      'evaded_sha256': 'f916a8443ccc2c08e8f2d1188d0ce03f4b26248c5de0aa8308a1e3862bd041e9'}), (
                  'Backdoor.Win32.Poison.cvk', {
                      'actions': ['ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Poison.a', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARI'], 'evaded': True,
        'evaded_sha256': '36a5cd9dd5063ef0bf7e66ebe1ac0071a532fd92e15eebab299fdc4bff7dabca'}), (
                  'Backdoor.Win32.PcClient.hmy', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI'],
                      'evaded': False}), ('Backdoor.Win32.Nepoe.fb', {
        'actions': ['ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS'],
        'evaded': True, 'evaded_sha256': 'c3fa7822780f73864a773acba21f27bfc228f96c6c496c662045f25d9a546e57'}), (
                  'Backdoor.Win32.PcClient.anh', {'actions': ['ARS'], 'evaded': True,
                                                  'evaded_sha256': '6c36e7e04082694d75ea949f2390009830af3943f8efcdb1f0124cd0557d09c3'}),
                  ('Backdoor.Win32.PcClient.dpv', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARI', 'RS',
                                  'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS'], 'evaded': True,
                      'evaded_sha256': '897546796bc997486b361c8db3fc27bd84a00581104bddbb7728bada669ff1ca'}), (
                  'Backdoor.Win32.PcClient.hj', {'actions': ['ARS'], 'evaded': True,
                                                 'evaded_sha256': 'd1d0859abd734f95742a4dc539f48771702b86e0aa786b3a43c425e8b66f31e0'}),
                  ('Backdoor.Win32.Loony.d', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE',
                                  'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARBE', 'ARBE', 'ARI', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARBE', 'ARBE', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                                  'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.reu', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.Hupigon.ztl', {
        'actions': ['RS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARBE',
                    'ARS', 'ARS', 'ARBE', 'ARBE', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI',
                    'ARI', 'ARI', 'ARI', 'ARI'], 'evaded': False}), ('Backdoor.Win32.PcClient.lpq', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                    'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': '931c16149870ac4ee703f0b9491fee629ba408d0767b9ec24e252bf53de0ea29'}), (
                  'Backdoor.Win32.Kbot.dl', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.PcClient.mnp', {'actions': ['ARS'], 'evaded': True,
                                                                          'evaded_sha256': 'c6062db53c04ddf62a90ba4b5ceb6c4ef57ad7c7250cf79e4d88c2b5ab3ddb8b'}),
                  ('Backdoor.Win32.PcClient.ggq', {
                      'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARBE', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARI',
                                  'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'ARS'],
                      'evaded': False}), ('Backdoor.Win32.Nucleroot.c', {
        'actions': ['ARS', 'ARS', 'ARS', 'ARS', 'ARS', 'RS', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS', 'ARI', 'ARI', 'ARS',
                    'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARI', 'ARS', 'ARS', 'ARS'], 'evaded': True,
        'evaded_sha256': 'e9c3028d78593fe9a725bc305ee6cde00bd3aeda6ecaf2910497234e3e5c51c0'})])

count = 0
success = 0
for k, v in dd.items():
    # shutil.copy(os.path.join(interface.SAMPLEPATH, k), 'samples')
    # count += 1
    # if dd[k]['evaded']:
    #     success += 1
    #     print("{}:{}->{}".format(count, k, v['evadedsha256']))
    #     shutil.copy(os.path.join(interface.EVADEDSAMPLEPATH, v['evadedsha256']), 'evaded')
    # else:
    #     print("{}:{}->".format(count, k))
    count += 1
    episode = dd[k]
    if (episode['evaded']) and len(episode['actions']) > 10:
        success += 1
        print("{}&{}&{}&success \\\\ \hline".format(success, k, dd[k]['actions']))
