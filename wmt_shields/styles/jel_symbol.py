# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2011-2020 Sarah Hoffmann
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import os

from ..common.tags import Tags
from ..common.config import ShieldConfig
from .image_symbol import ImageSymbol

def create_for(tags: Tags, region: str, config: ShieldConfig):
    ref = tags.get('jel')
    if ref is None or ref not in config.jel_types:
        return None

    uuid = f'jel_{{}}_{ref}'
    fn = os.path.join(config.jel_path, f'{ref}.svg')
    return ImageSymbol(uuid, fn, config)
