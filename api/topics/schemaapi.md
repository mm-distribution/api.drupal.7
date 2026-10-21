# Schema API

- **Topic id:** `schemaapi`
- **Defined in:** [`includes/database/schema.inc`](../includes/database/schema.inc/_file.md), line 10 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L10)

## Documentation

```text
@defgroup schemaapi Schema API
@{
API to handle database schemas.

A Drupal schema definition is an array structure representing one or
more tables and their related keys and indexes. A schema is defined by
hook_schema(), which usually lives in a modulename.install file.

By implementing hook_schema() and specifying the tables your module
declares, you can easily create and drop these tables on all
supported database engines. You don't have to deal with the
different SQL dialects for table creation and alteration of the
supported database engines.

hook_schema() should return an array with a key for each table that
the module defines.

The following keys are defined:
  - 'description': A string in non-markup plain text describing this table
    and its purpose. References to other tables should be enclosed in
    curly-brackets. For example, the node_revisions table
    description field might contain "Stores per-revision title and
    body data for each {node}."
  - 'fields': An associative array ('fieldname' => specification)
    that describes the table's database columns. The specification
    is also an array. The following specification parameters are defined:
    - 'description': A string in non-markup plain text describing this field
      and its purpose. References to other tables should be enclosed in
      curly-brackets. For example, the node table vid field
      description might contain "Always holds the largest (most
      recent) {node_revision}.vid value for this nid."
    - 'type': The generic datatype: 'char', 'varchar', 'text', 'blob', 'int',
      'float', 'numeric', or 'serial'. Most types just map to the according
      database engine specific datatypes. Use 'serial' for auto incrementing
      fields. This will expand to 'INT auto_increment' on MySQL.
    - 'mysql_type', 'pgsql_type', 'sqlite_type', etc.: If you need to
      use a record type not included in the officially supported list
      of types above, you can specify a type for each database
      backend. In this case, you can leave out the type parameter,
      but be advised that your schema will fail to load on backends that
      do not have a type specified. A possible solution can be to
      use the "text" type as a fallback.
    - 'serialize': A boolean indicating whether the field will be stored as
      a serialized string.
    - 'size': The data size: 'tiny', 'small', 'medium', 'normal',
      'big'. This is a hint about the largest value the field will
      store and determines which of the database engine specific
      datatypes will be used (e.g. on MySQL, TINYINT vs. INT vs. BIGINT).
      'normal', the default, selects the base type (e.g. on MySQL,
      INT, VARCHAR, BLOB, etc.).
      Not all sizes are available for all data types. See
      DatabaseSchema::getFieldTypeMap() for possible combinations.
    - 'not null': If true, no NULL values will be allowed in this
      database column. Defaults to false.
    - 'default': The field's default value. The PHP type of the
      value matters: '', '0', and 0 are all different. If you
      specify '0' as the default value for a type 'int' field it
      will not work because '0' is a string containing the
      character "zero", not an integer.
    - 'length': The maximal length of a type 'char', 'varchar' or 'text'
      field. Ignored for other field types.
    - 'unsigned': A boolean indicating whether a type 'int', 'float'
      and 'numeric' only is signed or unsigned. Defaults to
      FALSE. Ignored for other field types.
    - 'precision', 'scale': For type 'numeric' fields, indicates
      the precision (total number of significant digits) and scale
      (decimal digits right of the decimal point). Both values are
      mandatory. Ignored for other field types.
    - 'binary': A boolean indicating that MySQL should force 'char',
      'varchar' or 'text' fields to use case-sensitive binary collation.
      This has no effect on other database types for which case sensitivity
      is already the default behavior.
    All parameters apart from 'type' are optional except that type
    'numeric' columns must specify 'precision' and 'scale', and type
    'varchar' must specify the 'length' parameter.
 - 'primary key': An array of one or more key column specifiers (see below)
   that form the primary key.
 - 'unique keys': An associative array of unique keys ('keyname' =>
   specification). Each specification is an array of one or more
   key column specifiers (see below) that form a unique key on the table.
 - 'foreign keys': An associative array of relations ('my_relation' =>
   specification). Each specification is an array containing the name of
   the referenced table ('table'), and an array of column mappings
   ('columns'). Column mappings are defined by key pairs ('source_column' =>
   'referenced_column'). This key is for documentation purposes only; foreign
   keys are not created in the database, nor are they enforced by Drupal.
 - 'indexes':  An associative array of indexes ('indexname' =>
   specification). Each specification is an array of one or more
   key column specifiers (see below) that form an index on the
   table.

A key column specifier is either a string naming a column or an
array of two elements, column name and length, specifying a prefix
of the named column.

As an example, here is a SUBSET of the schema definition for
Drupal's 'node' table. It show four fields (nid, vid, type, and
title), the primary key on field 'nid', a unique key named 'vid' on
field 'vid', and two indexes, one named 'nid' on field 'nid' and
one named 'node_title_type' on the field 'title' and the first four
bytes of the field 'type':

@code
$schema['node'] = array(
  'description' => 'The base table for nodes.',
  'fields' => array(
    'nid'       => array('type' => 'serial', 'unsigned' => TRUE, 'not null' => TRUE),
    'vid'       => array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE,'default' => 0),
    'type'      => array('type' => 'varchar','length' => 32,'not null' => TRUE, 'default' => ''),
    'language'  => array('type' => 'varchar','length' => 12,'not null' => TRUE,'default' => ''),
    'title'     => array('type' => 'varchar','length' => 255,'not null' => TRUE, 'default' => ''),
    'uid'       => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'status'    => array('type' => 'int', 'not null' => TRUE, 'default' => 1),
    'created'   => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'changed'   => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'comment'   => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'promote'   => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'moderate'  => array('type' => 'int', 'not null' => TRUE,'default' => 0),
    'sticky'    => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
    'tnid'      => array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE, 'default' => 0),
    'translate' => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
  ),
  'indexes' => array(
    'node_changed'        => array('changed'),
    'node_created'        => array('created'),
    'node_moderate'       => array('moderate'),
    'node_frontpage'      => array('promote', 'status', 'sticky', 'created'),
    'node_status_type'    => array('status', 'type', 'nid'),
    'node_title_type'     => array('title', array('type', 4)),
    'node_type'           => array(array('type', 4)),
    'uid'                 => array('uid'),
    'tnid'                => array('tnid'),
    'translate'           => array('translate'),
  ),
  'unique keys' => array(
    'vid' => array('vid'),
  ),
  // For documentation purposes only; foreign keys are not created in the
  // database.
  'foreign keys' => array(
    'node_revision' => array(
      'table' => 'node_revision',
      'columns' => array('vid' => 'vid'),
     ),
    'node_author' => array(
      'table' => 'users',
      'columns' => array('uid' => 'uid'),
     ),
   ),
  'primary key' => array('nid'),
);
@endcode

@see drupal_install_schema()
```

## Members (derived, 97)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_db_create_keys_sql()](../includes/database/database.inc/_db_create_keys_sql.md) (function)
- [_drupal_schema_initialize()](../includes/common.inc/_drupal_schema_initialize.md) (function) — Fills in required default values for table definitions from hook_schema().
- [db_add_field()](../includes/database/database.inc/db_add_field.md) (function) — Adds a new field to a table.
- [db_add_index()](../includes/database/database.inc/db_add_index.md) (function) — Adds an index.
- [db_add_primary_key()](../includes/database/database.inc/db_add_primary_key.md) (function) — Adds a primary key to a database table.
- [db_add_unique_key()](../includes/database/database.inc/db_add_unique_key.md) (function) — Adds a unique key.
- [db_change_field()](../includes/database/database.inc/db_change_field.md) (function) — Changes a field definition.
- [db_create_table()](../includes/database/database.inc/db_create_table.md) (function) — Creates a new table from a Drupal table definition.
- [db_drop_field()](../includes/database/database.inc/db_drop_field.md) (function) — Drops a field.
- [db_drop_index()](../includes/database/database.inc/db_drop_index.md) (function) — Drops an index.
- [db_drop_primary_key()](../includes/database/database.inc/db_drop_primary_key.md) (function) — Drops the primary key of a database table.
- [db_drop_table()](../includes/database/database.inc/db_drop_table.md) (function) — Drops a table.
- [db_drop_unique_key()](../includes/database/database.inc/db_drop_unique_key.md) (function) — Drops a unique key.
- [db_field_exists()](../includes/database/database.inc/db_field_exists.md) (function) — Checks if a column exists in the given table.
- [db_field_names()](../includes/database/database.inc/db_field_names.md) (function) — Returns an array of field names from an array of key/index column specifiers.
- [db_field_set_default()](../includes/database/database.inc/db_field_set_default.md) (function) — Sets the default value for a field.
- [db_field_set_no_default()](../includes/database/database.inc/db_field_set_no_default.md) (function) — Sets a field to have no default value.
- [db_find_tables()](../includes/database/database.inc/db_find_tables.md) (function) — Finds all tables that are like the specified base table name.
- [db_find_tables_d8()](../includes/database/database.inc/db_find_tables_d8.md) (function) — Finds all tables that are like the specified base table name. This is a backport of the change made to db_find_tables in Drupal 8 to work with virtual, un-prefixed table names. The original function is retained for Backwards Compatibility.
- [db_index_exists()](../includes/database/database.inc/db_index_exists.md) (function) — Checks if an index exists in the given table.
- [db_rename_table()](../includes/database/database.inc/db_rename_table.md) (function) — Renames a table.
- [db_table_exists()](../includes/database/database.inc/db_table_exists.md) (function) — Checks if a table exists.
- [drupal_get_complete_schema()](../includes/bootstrap.inc/drupal_get_complete_schema.md) (function) — Gets the whole database schema.
- [drupal_get_schema()](../includes/bootstrap.inc/drupal_get_schema.md) (function) — Gets the schema definition of a table, or the whole database schema.
- [drupal_get_schema_unprocessed()](../includes/common.inc/drupal_get_schema_unprocessed.md) (function) — Returns the unprocessed and unaltered version of a module's schema.
- [drupal_install_schema()](../includes/common.inc/drupal_install_schema.md) (function) — Creates all tables defined in a module's hook_schema().
- [drupal_schema_field_types()](../includes/common.inc/drupal_schema_field_types.md) (function) — Retrieves the type for every field in a table schema.
- [drupal_schema_fields_sql()](../includes/common.inc/drupal_schema_fields_sql.md) (function) — Retrieves a list of fields from a table schema.
- [drupal_uninstall_schema()](../includes/common.inc/drupal_uninstall_schema.md) (function) — Removes all tables defined in a module's hook_schema().
- [drupal_write_record()](../includes/common.inc/drupal_write_record.md) (function) — Saves (inserts or updates) a record to the database based upon the schema.
- [hook_schema()](../modules/system/system.api.php/hook_schema.md) (function) — Define the current version of the database schema.
- [hook_schema_alter()](../modules/system/system.api.php/hook_schema_alter.md) (function) — Perform alterations to existing database schemas.
- [DatabaseSchema](../includes/database/schema.inc/DatabaseSchema.md) (class) — Base class for database schema definitions.
- [DatabaseSchemaObjectDoesNotExistException](../includes/database/schema.inc/DatabaseSchemaObjectDoesNotExistException.md) (class) — Exception thrown if an object being modified doesn't exist yet.
- [DatabaseSchemaObjectExistsException](../includes/database/schema.inc/DatabaseSchemaObjectExistsException.md) (class) — Exception thrown if an object being created already exists.
- [DatabaseSchema_mysql](../includes/database/mysql/schema.inc/DatabaseSchema_mysql.md) (class)
- [DatabaseSchema_pgsql](../includes/database/pgsql/schema.inc/DatabaseSchema_pgsql.md) (class)
- [DatabaseSchema_sqlite](../includes/database/sqlite/schema.inc/DatabaseSchema_sqlite.md) (class)
- [SchemaCache](../includes/bootstrap.inc/SchemaCache.md) (class) — Extends DrupalCacheArray to allow for dynamic building of the schema cache.
- [DatabaseSchema::__clone()](../includes/database/schema.inc/DatabaseSchema/__clone.md) (method) — Implements the magic __clone function.
- [DatabaseSchema::__construct()](../includes/database/schema.inc/DatabaseSchema/__construct.md) (method)
- [DatabaseSchema::addField()](../includes/database/schema.inc/DatabaseSchema/addField.md) (method) — Add a new field to a table.
- [DatabaseSchema::addIndex()](../includes/database/schema.inc/DatabaseSchema/addIndex.md) (method) — Add an index.
- [DatabaseSchema::addPrimaryKey()](../includes/database/schema.inc/DatabaseSchema/addPrimaryKey.md) (method) — Add a primary key.
- [DatabaseSchema::addUniqueKey()](../includes/database/schema.inc/DatabaseSchema/addUniqueKey.md) (method) — Add a unique key.
- [DatabaseSchema::buildTableNameCondition()](../includes/database/schema.inc/DatabaseSchema/buildTableNameCondition.md) (method) — Build a condition to match a table name against a standard information_schema.
- [DatabaseSchema::changeField()](../includes/database/schema.inc/DatabaseSchema/changeField.md) (method) — Change a field definition.
- [DatabaseSchema::createTable()](../includes/database/schema.inc/DatabaseSchema/createTable.md) (method) — Create a new table from a Drupal table definition.
- [DatabaseSchema::dropField()](../includes/database/schema.inc/DatabaseSchema/dropField.md) (method) — Drop a field.
- [DatabaseSchema::dropIndex()](../includes/database/schema.inc/DatabaseSchema/dropIndex.md) (method) — Drop an index.
- [DatabaseSchema::dropPrimaryKey()](../includes/database/schema.inc/DatabaseSchema/dropPrimaryKey.md) (method) — Drop the primary key.
- [DatabaseSchema::dropTable()](../includes/database/schema.inc/DatabaseSchema/dropTable.md) (method) — Drop a table.
- [DatabaseSchema::dropUniqueKey()](../includes/database/schema.inc/DatabaseSchema/dropUniqueKey.md) (method) — Drop a unique key.
- [DatabaseSchema::fieldExists()](../includes/database/schema.inc/DatabaseSchema/fieldExists.md) (method) — Check if a column exists in the given table.
- [DatabaseSchema::fieldNames()](../includes/database/schema.inc/DatabaseSchema/fieldNames.md) (method) — Return an array of field names from an array of key/index column specifiers.
- [DatabaseSchema::fieldSetDefault()](../includes/database/schema.inc/DatabaseSchema/fieldSetDefault.md) (method) — Set the default value for a field.
- [DatabaseSchema::fieldSetNoDefault()](../includes/database/schema.inc/DatabaseSchema/fieldSetNoDefault.md) (method) — Set a field to have no default value.
- [DatabaseSchema::findTables()](../includes/database/schema.inc/DatabaseSchema/findTables.md) (method) — Find all tables that are like the specified base table name.
- [DatabaseSchema::findTablesD8()](../includes/database/schema.inc/DatabaseSchema/findTablesD8.md) (method) — Finds all tables that are like the specified base table name. This is a backport of the change made to findTables in Drupal 8 to work with virtual, un-prefixed table names. The original function is retained for Backwards Compatibility.
- [DatabaseSchema::getFieldTypeMap()](../includes/database/schema.inc/DatabaseSchema/getFieldTypeMap.md) (method) — Returns a mapping of Drupal schema field names to DB-native field types.
- [DatabaseSchema::getPrefixInfo()](../includes/database/schema.inc/DatabaseSchema/getPrefixInfo.md) (method) — Get information about the table name and schema from the prefix.
- [DatabaseSchema::indexExists()](../includes/database/schema.inc/DatabaseSchema/indexExists.md) (method) — Checks if an index exists in the given table.
- [DatabaseSchema::nextPlaceholder()](../includes/database/schema.inc/DatabaseSchema/nextPlaceholder.md) (method) — Implements QueryPlaceHolderInterface::nextPlaceholder().
- [DatabaseSchema::prefixNonTable()](../includes/database/schema.inc/DatabaseSchema/prefixNonTable.md) (method) — Create names for indexes, primary keys and constraints.
- [DatabaseSchema::prepareComment()](../includes/database/schema.inc/DatabaseSchema/prepareComment.md) (method) — Prepare a table or column comment for database query.
- [DatabaseSchema::renameTable()](../includes/database/schema.inc/DatabaseSchema/renameTable.md) (method) — Rename a table.
- [DatabaseSchema::tableExists()](../includes/database/schema.inc/DatabaseSchema/tableExists.md) (method) — Check if a table exists.
- [DatabaseSchema::uniqueIdentifier()](../includes/database/schema.inc/DatabaseSchema/uniqueIdentifier.md) (method) — Implements QueryPlaceHolderInterface::uniqueIdentifier().
- [DatabaseSchema_mysql::addField()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/addField.md) (method)
- [DatabaseSchema_mysql::addIndex()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/addIndex.md) (method)
- [DatabaseSchema_mysql::addPrimaryKey()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/addPrimaryKey.md) (method)
- [DatabaseSchema_mysql::addUniqueKey()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/addUniqueKey.md) (method)
- [DatabaseSchema_mysql::buildTableNameCondition()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/buildTableNameCondition.md) (method) — Build a condition to match a table name against a standard information_schema.
- [DatabaseSchema_mysql::changeField()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/changeField.md) (method)
- [DatabaseSchema_mysql::createFieldSql()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/createFieldSql.md) (method) — Create an SQL string for a field to be used in table creation or alteration.
- [DatabaseSchema_mysql::createKeySql()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/createKeySql.md) (method)
- [DatabaseSchema_mysql::createKeysSql()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/createKeysSql.md) (method)
- [DatabaseSchema_mysql::createKeysSqlHelper()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/createKeysSqlHelper.md) (method)
- [DatabaseSchema_mysql::createTableSql()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/createTableSql.md) (method) — Generate SQL to create a new table from a Drupal schema definition.
- [DatabaseSchema_mysql::dropField()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/dropField.md) (method)
- [DatabaseSchema_mysql::dropIndex()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/dropIndex.md) (method)
- [DatabaseSchema_mysql::dropPrimaryKey()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/dropPrimaryKey.md) (method)
- [DatabaseSchema_mysql::dropTable()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/dropTable.md) (method)
- [DatabaseSchema_mysql::dropUniqueKey()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/dropUniqueKey.md) (method)
- [DatabaseSchema_mysql::fieldExists()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/fieldExists.md) (method)
- [DatabaseSchema_mysql::fieldSetDefault()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/fieldSetDefault.md) (method)
- [DatabaseSchema_mysql::fieldSetNoDefault()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/fieldSetNoDefault.md) (method)
- [DatabaseSchema_mysql::getComment()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/getComment.md) (method) — Retrieve a table or column comment.
- [DatabaseSchema_mysql::getFieldTypeMap()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/getFieldTypeMap.md) (method)
- [DatabaseSchema_mysql::getPrefixInfo()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/getPrefixInfo.md) (method) — Get information about the table and database name from the prefix.
- [DatabaseSchema_mysql::indexExists()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/indexExists.md) (method)
- [DatabaseSchema_mysql::prepareComment()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/prepareComment.md) (method)
- [DatabaseSchema_mysql::processField()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/processField.md) (method) — Set database-engine specific properties for a field.
- [DatabaseSchema_mysql::renameTable()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/renameTable.md) (method)
- [DatabaseSchema_mysql::tableExists()](../includes/database/mysql/schema.inc/DatabaseSchema_mysql/tableExists.md) (method)
- [SchemaCache::__construct()](../includes/bootstrap.inc/SchemaCache/__construct.md) (method) — Constructs a SchemaCache object.
- [SchemaCache::resolveCacheMiss()](../includes/bootstrap.inc/SchemaCache/resolveCacheMiss.md) (method) — Overrides DrupalCacheArray::resolveCacheMiss().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
