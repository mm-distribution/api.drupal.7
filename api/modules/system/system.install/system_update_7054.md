# system_update_7054()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2608–2624 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2608-L2624)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7054()
```

## Documentation

```text
Remove {cache_*}.headers columns.
```

## Code

```php
function system_update_7054() {
  // Update: update_fix_d7_requirements() installs this version for cache_path
  // already, so we don't include it in this particular update. It should be
  // included in later updates though.
  $cache_tables = array(
    'cache' => 'Generic cache table for caching things not separated out into their own tables. Contributed modules may also use this to store cached items.',
    'cache_form' => 'Cache table for the form system to store recently built forms and their storage data, to be used in subsequent page requests.',
    'cache_page' => 'Cache table used to store compressed pages for anonymous users, if page caching is enabled.',
    'cache_menu' => 'Cache table for the menu system to store router information as well as generated link trees for various menu/page/user combinations.',
  );
  $schema = system_schema_cache_7054();
  foreach ($cache_tables as $table => $description) {
    $schema['description'] = $description;
    db_drop_table($table);
    db_create_table($table, $schema);
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
