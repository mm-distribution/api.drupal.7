# system_update_7042()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2440–2460 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2440-L2460)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7042()
```

## Documentation

```text
Upgrade the {url_alias} table and create a cache bin for path aliases.
```

## Code

```php
function system_update_7042() {
  // update_fix_d7_requirements() adds 'fake' source and alias columns to
  // allow bootstrap to run without fatal errors. Remove those columns now
  // so that we can rename properly.
  db_drop_field('url_alias', 'source');
  db_drop_field('url_alias', 'alias');

  // Drop indexes.
  db_drop_index('url_alias', 'src_language_pid');
  db_drop_unique_key('url_alias', 'dst_language_pid');
  // Rename the fields, and increase their length to 255 characters.
  db_change_field('url_alias', 'src', 'source', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));
  db_change_field('url_alias', 'dst', 'alias', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));
  // Add indexes back. We replace the unique key with an index since it never
  // provided any meaningful unique constraint ('pid' is a primary key).
  db_add_index('url_alias', 'source_language_pid', array('source', 'language', 'pid'));
  db_add_index('url_alias', 'alias_language_pid', array('alias', 'language', 'pid'));

  // Now that the URL aliases are correct, we can rebuild the whitelist.
  drupal_path_alias_whitelist_rebuild();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
