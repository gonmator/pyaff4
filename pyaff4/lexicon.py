# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.

"""The AFF4 lexicon."""
#define AFF4_VERSION "0.1"


AFF4_NAMESPACE = "http://afflib.org/2009/aff4#"
XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema#"
RDF_NAMESPACE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

# Attributes in this namespace will never be written to persistant
# storage. They are simply used as a way for storing metadata about an AFF4
# object internally.
AFF4_VOLATILE_NAMESPACE = "Volatile:"

# Attribute names for different AFF4 objects.
# Base AFF4Object
AFF4_TYPE = (RDF_NAMESPACE + "type")
AFF4_STORED = (AFF4_NAMESPACE + "stored")

# AFF4 ZipFile containers.
AFF4_ZIP_TYPE = (AFF4_NAMESPACE + "zip_volume")

# AFF4Stream
AFF4_STREAM_SIZE = (AFF4_NAMESPACE + "size")

# Can be "read", "truncate", "append"
AFF4_STREAM_WRITE_MODE = (AFF4_VOLATILE_NAMESPACE + "writable")

# ZipFileSegment
AFF4_ZIP_SEGMENT_TYPE = (AFF4_NAMESPACE + "zip_segment")

# AFF4Image - stores a stream using Bevies.
AFF4_IMAGE_TYPE = (AFF4_NAMESPACE + "image")
AFF4_IMAGE_CHUNK_SIZE = (AFF4_NAMESPACE + "chunk_size")
AFF4_IMAGE_CHUNKS_PER_SEGMENT = (AFF4_NAMESPACE + "chunks_per_segment")
AFF4_IMAGE_COMPRESSION = (AFF4_NAMESPACE + "compression")
AFF4_IMAGE_COMPRESSION_DEFLATE = "https://www.ietf.org/rfc/rfc1951.txt"

# AFF4Map - stores a mapping from one stream to another.
AFF4_MAP_TYPE = (AFF4_NAMESPACE + "map")
