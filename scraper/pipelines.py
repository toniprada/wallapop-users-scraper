# -*- coding: utf-8 -*-
import json
import os

class JsonWriterPipeline(object):

    def process_item(self, item, spider):
        user_id = str(item['profile']['userId'])
        folder = 'output/%s' % '/'.join(list(user_id)[:3])
        if not os.path.exists(folder): os.makedirs(folder)
        filename = '%s/user_%s.json' % (folder, user_id)
        with open(filename, 'w+') as f: json.dump(dict(item), f)
        return item
