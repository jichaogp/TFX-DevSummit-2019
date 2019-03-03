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
"""Utilities for retrieving paths for various types of artifacts."""
import os

from tfx.utils import io_utils

EVAL_MODEL_DIR = 'eval_model_dir'
SERVING_MODEL_DIR = 'serving_model_dir'


def eval_model_dir(output_uri):
  """Returns directory for exported model for evaluation purpose."""
  return os.path.join(output_uri, EVAL_MODEL_DIR)


def eval_model_path(output_uri):
  """Returns path to timestamped exported model for evaluation purpose."""
  model_dir = eval_model_dir(output_uri)
  return io_utils.get_only_uri_in_dir(model_dir)


def serving_model_dir(output_uri):
  """Returns directory for exported model for serving purpose."""
  return os.path.join(output_uri, SERVING_MODEL_DIR)


def serving_model_path(output_uri):
  """Returns path for timestamped and named serving model exported."""
  export_dir = os.path.join(serving_model_dir(output_uri), 'export')
  model_dir = io_utils.get_only_uri_in_dir(export_dir)
  return io_utils.get_only_uri_in_dir(model_dir)
