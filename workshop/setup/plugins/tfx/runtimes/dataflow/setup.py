# Copyright 2019Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup dependencies for local and cloud deployment."""
import setuptools

if __name__ == '__main__':
  setuptools.setup(
      name='tfx-cloud-runner',
      version='0.2.1',
      packages=setuptools.find_packages(),
      install_requires=[
          'apache-beam[gcp]==2.8.0',
          'jupyter==1.0',
          'numpy==1.14.5',
          'protobuf==3.6.0',
          'tensorflow==1.11.0',
          'tensorflow-data-validation==0.11.0',
          'tensorflow-metadata==0.9.0',
          'tensorflow-model-analysis==0.11.0',
          'tensorflow-serving-api==1.11.0',
          'tensorflow-transform==0.11.0',
          'ml-metadata',
      ])
