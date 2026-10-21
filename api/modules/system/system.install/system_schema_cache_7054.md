# system_schema_cache_7054()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1810–1852 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1810-L1852)
- **Module/theme:** system

## Signature

```php
function system_schema_cache_7054()
```

## Documentation

```text
The cache schema corresponding to system_update_7054.

Drupal 7 adds several new cache tables. Since they all have identical schema
this helper function allows them to re-use the same definition, without
relying on system_schema(), which may change with future updates.
```

## Code

```php
function system_schema_cache_7054() {
  return array(
    'description' => 'Generic cache table for caching things not separated out into their own tables. Contributed modules may also use this to store cached items.',
    'fields' => array(
      'cid' => array(
        'description' => 'Primary Key: Unique cache ID.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'data' => array(
        'description' => 'A collection of data to cache.',
        'type' => 'blob',
        'not null' => FALSE,
        'size' => 'big',
      ),
      'expire' => array(
        'description' => 'A Unix timestamp indicating when the cache entry should expire, or 0 for never.',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
      ),
      'created' => array(
        'description' => 'A Unix timestamp indicating when the cache entry was created.',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
      ),
      'serialized' => array(
        'description' => 'A flag to indicate whether content is serialized (1) or not (0).',
        'type' => 'int',
        'size' => 'small',
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'indexes' => array(
      'expire' => array('expire'),
    ),
    'primary key' => array('cid'),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
