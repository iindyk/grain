# Copyright 2024 Google LLC
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
"""Proto PyGrain APIs."""

# pylint: disable=g-importing-member
# pylint: disable=g-multiple-import
# pylint: disable=unused-import

from grain._src.python.proto.decode import (
    parse_tf_example,
    parse_tf_example_experimental,
)
from grain._src.python.proto.encode import make_tf_example
