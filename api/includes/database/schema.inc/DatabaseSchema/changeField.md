# DatabaseSchema::changeField()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 716–716 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L716)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function changeField($table, $field, $field_new, $spec, $keys_new = array());
```

## Documentation

```text
Change a field definition.

IMPORTANT NOTE: To maintain database portability, you have to explicitly
recreate all indices and primary keys that are using the changed field.

That means that you have to drop all affected keys and indexes with
db_drop_{primary_key,unique_key,index}() before calling db_change_field().
To recreate the keys and indices, pass the key definitions as the
optional $keys_new argument directly to db_change_field().

For example, suppose you have:
@code
$schema['foo'] = array(
  'fields' => array(
    'bar' => array('type' => 'int', 'not null' => TRUE)
  ),
  'primary key' => array('bar')
);
@endcode
and you want to change foo.bar to be type serial, leaving it as the
primary key. The correct sequence is:
@code
db_drop_primary_key('foo');
db_change_field('foo', 'bar', 'bar',
  array('type' => 'serial', 'not null' => TRUE),
  array('primary key' => array('bar')));
@endcode

The reasons for this are due to the different database engines:

On PostgreSQL, changing a field definition involves adding a new field
and dropping an old one which* causes any indices, primary keys and
sequences (from serial-type fields) that use the changed field to be dropped.

On MySQL, all type 'serial' fields must be part of at least one key
or index as soon as they are created. You cannot use
db_add_{primary_key,unique_key,index}() for this purpose because
the ALTER TABLE command will fail to add the column without a key
or index specification. The solution is to use the optional
$keys_new argument to create the key or index at the same time as
field.

You could use db_add_{primary_key,unique_key,index}() in all cases
unless you are converting a field to be type serial. You can use
the $keys_new argument in all cases.

@param $table
  Name of the table.
@param $field
  Name of the field to change.
@param $field_new
  New name for the field (set to the same as $field if you don't want to change the name).
@param $spec
  The field specification for the new field.
@param $keys_new
  (optional) Keys and indexes specification to be created on the
  table along with changing the field. The format is the same as a
  table specification but without the 'fields' element.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table or source field doesn't exist.
@throws DatabaseSchemaObjectExistsException
  If the specified destination field already exists.
```

## Code

```php
  abstract public function changeField($table, $field, $field_new, $spec, $keys_new = array());
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
