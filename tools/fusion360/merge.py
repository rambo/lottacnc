#!/usr/bin/env python
from __future__ import with_statement, print_function
import json
from collections import OrderedDict


class tool_library_merger(object):
    _base_library = None
    _base_data_by_guid = None
    _merge_libraries = []
    _merge_data_by_guid = []

    def __init__(self, base, merges):
        with open(base, 'rb') as bp:
            self._base_library = json.load(bp, object_pairs_hook=OrderedDict)
            self._base_data_by_guid = self._key_by_guid(self._base_library['data'])
        for fname in merges:
            with open(fname, 'rb') as fp:
                self._merge_libraries.append(json.load(fp, object_pairs_hook=OrderedDict))
                self._merge_data_by_guid.append(self._key_by_guid(self._merge_libraries[-1]['data']))

    def _key_by_guid(self, source):
        target = OrderedDict()
        for sourcedata in source:
            target[sourcedata['guid']] = sourcedata
        return target

    def _merge_two(self, base, merge):
        for guid in merge:
            if guid not in base:
                base[guid] = merge[guid]
                continue
            base[guid].update(merge[guid])

    def merge(self, target_file):
        with open(target_file, 'wb') as tp:
            for new_lbr in self._merge_data_by_guid:
                self._merge_two(self._base_data_by_guid, new_lbr)
            new_library = self._base_library
            new_library['data'] = []
            for guid in self._base_data_by_guid:
                new_library['data'].append(self._base_data_by_guid[guid])
            new_library['version'] = self._merge_libraries[-1]['version']
            json.dump(new_library, tp, indent=2)



def usage(cmdname):
    print("""
Usage:
    {cmdname} base_library merge_library [merge_library2 ...] target_filename 
    """.format(cmdname=cmdname))



if __name__ == '__main__':
    import os,sys
    if len(sys.argv) < 4:
        usage(os.path.basename(sys.argv[0]))
        sys.exit(1)
    instance = tool_library_merger(sys.argv[1], sys.argv[1:-1])
    instance.merge(sys.argv[-1])
