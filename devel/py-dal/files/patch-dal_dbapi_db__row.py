
$FreeBSD: devel/py-dal/files/patch-dal_dbapi_db__row.py 300896 2012-07-14 13:54:48Z beat $

--- dal/dbapi/db_row.py
+++ dal/dbapi/db_row.py
@@ -699,7 +699,6 @@
     assert '__init__' not in cls_dict
 
     def __init__(self, fields):
-      super(row_class, self).__init__(fields)
       self.fields = field_class(fields)
 
     row_class.__init__ = __init__
