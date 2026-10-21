# hook_schema()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3221–3277 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3221-L3277)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function hook_schema()
```

## Documentation

```text
Define the current version of the database schema.

A Drupal schema definition is an array structure representing one or more
tables and their related keys and indexes. A schema is defined by
hook_schema() which must live in your module's .install file.

This hook is called at install and uninstall time, and in the latter case, it
cannot rely on the .module file being loaded or hooks being known. If the
.module file is needed, it may be loaded with drupal_load().

The tables declared by this hook will be automatically created when the
module is first enabled, and removed when the module is uninstalled. This
happens before hook_install() is invoked, and after hook_uninstall() is
invoked, respectively.

By declaring the tables used by your module via an implementation of
hook_schema(), these tables will be available on all supported database
engines. You don't have to deal with the different SQL dialects for table
creation and alteration of the supported database engines.

See the Schema API Handbook at http://drupal.org/node/146843 for details on
schema definition structures. Note that foreign key definitions are for
documentation purposes only; foreign keys are not created in the database,
nor are they enforced by Drupal.

@return array
  A schema definition structure array. For each element of the
  array, the key is a table name and the value is a table structure
  definition.

@see hook_schema_alter()

@ingroup schemaapi
```

## Code

```php
function hook_schema() {
  $schema['node'] = array(
    // Example (partial) specification for table "node".
    'description' => 'The base table for nodes.',
    'fields' => array(
      'nid' => array(
        'description' => 'The primary identifier for a node.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'vid' => array(
        'description' => 'The current {node_revision}.vid version identifier.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'type' => array(
        'description' => 'The {node_type} of this node.',
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
      ),
      'title' => array(
        'description' => 'The title of this node, always treated as non-markup plain text.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'indexes' => array(
      'node_changed'        => array('changed'),
      'node_created'        => array('created'),
    ),
    'unique keys' => array(
      'nid_vid' => array('nid', 'vid'),
      'vid'     => array('vid'),
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
  return $schema;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_schema()".

- [aggregator_schema()](../../aggregator/aggregator.install/aggregator_schema.md) — `modules/aggregator/aggregator.install`
- [database_test_schema()](../../simpletest/tests/database_test.install/database_test_schema.md) — `modules/simpletest/tests/database_test.install`
- [module_test_schema()](../../simpletest/tests/module_test.install/module_test_schema.md) — `modules/simpletest/tests/module_test.install`
- [system_test_schema()](../../simpletest/tests/system_test.install/system_test_schema.md) — `modules/simpletest/tests/system_test.install`
- [taxonomy_test_schema()](../../simpletest/tests/taxonomy_test.install/taxonomy_test_schema.md) — `modules/simpletest/tests/taxonomy_test.install`
- [block_schema()](../../block/block.install/block_schema.md) — `modules/block/block.install`
- [book_schema()](../../book/book.install/book_schema.md) — `modules/book/book.install`
- [comment_schema()](../../comment/comment.install/comment_schema.md) — `modules/comment/comment.install`
- [contact_schema()](../../contact/contact.install/contact_schema.md) — `modules/contact/contact.install`
- [dblog_schema()](../../dblog/dblog.install/dblog_schema.md) — `modules/dblog/dblog.install`
- [field_schema()](../../field/field.install/field_schema.md) — `modules/field/field.install`
- [field_sql_storage_schema()](../../field/modules/field_sql_storage/field_sql_storage.install/field_sql_storage_schema.md) — `modules/field/modules/field_sql_storage/field_sql_storage.install`
- [field_test_schema()](../../field/tests/field_test.install/field_test_schema.md) — `modules/field/tests/field_test.install`
- [filter_schema()](../../filter/filter.install/filter_schema.md) — `modules/filter/filter.install`
- [forum_schema()](../../forum/forum.install/forum_schema.md) — `modules/forum/forum.install`
- [image_schema()](../../image/image.install/image_schema.md) — `modules/image/image.install`
- [locale_schema()](../../locale/locale.install/locale_schema.md) — `modules/locale/locale.install`
- [menu_schema()](../../menu/menu.install/menu_schema.md) — `modules/menu/menu.install`
- [node_schema()](../../node/node.install/node_schema.md) — `modules/node/node.install`
- [node_access_test_schema()](../../node/tests/node_access_test.install/node_access_test_schema.md) — `modules/node/tests/node_access_test.install`
- [openid_schema()](../../openid/openid.install/openid_schema.md) — `modules/openid/openid.install`
- [poll_schema()](../../poll/poll.install/poll_schema.md) — `modules/poll/poll.install`
- [profile_schema()](../../profile/profile.install/profile_schema.md) — `modules/profile/profile.install`
- [rdf_schema()](../../rdf/rdf.install/rdf_schema.md) — `modules/rdf/rdf.install`
- [search_schema()](../../search/search.install/search_schema.md) — `modules/search/search.install`
- [shortcut_schema()](../../shortcut/shortcut.install/shortcut_schema.md) — `modules/shortcut/shortcut.install`
- [simpletest_schema()](../../simpletest/simpletest.install/simpletest_schema.md) — `modules/simpletest/simpletest.install`
- [statistics_schema()](../../statistics/statistics.install/statistics_schema.md) — `modules/statistics/statistics.install`
- [system_schema()](../system.install/system_schema.md) — `modules/system/system.install`
- [taxonomy_schema()](../../taxonomy/taxonomy.install/taxonomy_schema.md) — `modules/taxonomy/taxonomy.install`
- [tracker_schema()](../../tracker/tracker.install/tracker_schema.md) — `modules/tracker/tracker.install`
- [trigger_schema()](../../trigger/trigger.install/trigger_schema.md) — `modules/trigger/trigger.install`
- [update_schema()](../../update/update.install/update_schema.md) — `modules/update/update.install`
- [user_schema()](../../user/user.install/user_schema.md) — `modules/user/user.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
