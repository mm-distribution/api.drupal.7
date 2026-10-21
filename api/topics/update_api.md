# Update versions of API functions

- **Topic id:** `update_api`
- **Defined in:** [`modules/system/system.api.php`](../modules/system/system.api.php/_file.md), line 4944 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4944)

## Documentation

```text
@defgroup update_api Update versions of API functions
@{
Functions that are similar to normal API functions, but do not invoke hooks.

These simplified versions of core API functions are provided for use by
update functions (hook_update_N() implementations).

During database updates the schema of any module could be out of date. For
this reason, caution is needed when using any API function within an update
function - particularly CRUD functions, functions that depend on the schema
(for example by using drupal_write_record()), and any functions that invoke
hooks.

Instead, a simplified utility function should be used. If a utility version
of the API function you require does not already exist, then you should
create a new function. The new utility function should be named
_update_N_mymodule_my_function(). N is the schema version the function acts
on (the schema version is the number N from the hook_update_N()
implementation where this schema was introduced, or a number following the
same numbering scheme), and mymodule_my_function is the name of the original
API function including the module's name.

Examples:
- _update_6000_mymodule_save(): This function performs a save operation
  without invoking any hooks using the 6.x schema.
- _update_7000_mymodule_save(): This function performs the same save
  operation using the 7.x schema.

The utility function should not invoke any hooks, and should perform database
operations using functions from the
@link database Database abstraction layer, @endlink
like db_insert(), db_update(), db_delete(), db_query(), and so on.

If a change to the schema necessitates a change to the utility function, a
new function should be created with a name based on the version of the schema
it acts on. See _update_7000_bar_get_types() and _update_7001_bar_get_types()
in the code examples that follow.

For example, foo.install could contain:
@code
function foo_update_dependencies() {
  // foo_update_7010() needs to run after bar_update_7000().
  $dependencies['foo'][7010] = array(
    'bar' => 7000,
  );

  // foo_update_7036() needs to run after bar_update_7001().
  $dependencies['foo'][7036] = array(
    'bar' => 7001,
  );

  return $dependencies;
}

function foo_update_7000() {
  // No updates have been run on the {bar_types} table yet, so this needs
  // to work with the 6.x schema.
  foreach (_update_6000_bar_get_types() as $type) {
    // Rename a variable.
  }
}

function foo_update_7010() {
   // Since foo_update_7010() is going to run after bar_update_7000(), it
   // needs to operate on the new schema, not the old one.
   foreach (_update_7000_bar_get_types() as $type) {
     // Rename a different variable.
   }
}

function foo_update_7036() {
  // This update will run after bar_update_7001().
  foreach (_update_7001_bar_get_types() as $type) {
  }
}
@endcode

And bar.install could contain:
@code
function bar_update_7000() {
  // Type and bundle are confusing, so we renamed the table.
  db_rename_table('bar_types', 'bar_bundles');
}

function bar_update_7001() {
  // Database table names should be singular when possible.
  db_rename_table('bar_bundles', 'bar_bundle');
}

function _update_6000_bar_get_types() {
  db_query('SELECT * FROM {bar_types}')->fetchAll();
}

function _update_7000_bar_get_types() {
  db_query('SELECT * FROM {bar_bundles'})->fetchAll();
}

function _update_7001_bar_get_types() {
  db_query('SELECT * FROM {bar_bundle}')->fetchAll();
}
@endcode

@see hook_update_N()
@see hook_update_dependencies()
```

## Members (derived, 9)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_update_7000_field_create_field()](../modules/field/field.install/_update_7000_field_create_field.md) (function) — Utility function: create a field by writing directly to the database.
- [_update_7000_field_create_instance()](../modules/field/field.install/_update_7000_field_create_instance.md) (function) — Utility function: write a field instance directly to the database.
- [_update_7000_field_delete_field()](../modules/field/field.install/_update_7000_field_delete_field.md) (function) — Utility function: delete a field stored in SQL storage directly from the database.
- [_update_7000_field_delete_instance()](../modules/field/field.install/_update_7000_field_delete_instance.md) (function) — Utility function: delete an instance and all its data of a field stored in SQL Storage.
- [_update_7000_field_read_fields()](../modules/field/field.install/_update_7000_field_read_fields.md) (function) — Utility function: fetch all the field definitions from the database.
- [_update_7000_field_sql_storage_write()](../modules/field/modules/field_sql_storage/field_sql_storage.install/_update_7000_field_sql_storage_write.md) (function) — Utility function: write field data directly to SQL storage.
- [_update_7000_node_get_types()](../modules/node/node.install/_update_7000_node_get_types.md) (function) — Utility function: fetch the node types directly from the database.
- [_update_7000_user_role_grant_permissions()](../modules/user/user.install/_update_7000_user_role_grant_permissions.md) (function) — Utility function: grant a set of permissions to a role during update.
- [_update_7002_taxonomy_get_vocabularies()](../modules/taxonomy/taxonomy.install/_update_7002_taxonomy_get_vocabularies.md) (function) — Utility function: get the list of vocabularies directly from the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
