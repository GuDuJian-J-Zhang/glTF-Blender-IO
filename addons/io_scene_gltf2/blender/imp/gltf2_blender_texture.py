# Copyright 2018 The glTF-Blender-IO authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .gltf2_blender_image import BlenderImage


class BlenderTextureInfo():
    """Blender Texture info."""

    @staticmethod
    def create(gltf, pytextureinfo_idx):
        """Create Texture info."""
        BlenderTexture.create(gltf, pytextureinfo_idx)


class BlenderTexture():
    """Blender Texture."""

    @staticmethod
    def create(gltf, pytexture_idx):
        """Create texture."""
        pytexture = gltf.data.textures[pytexture_idx]
        BlenderImage.create(gltf, pytexture.source)
