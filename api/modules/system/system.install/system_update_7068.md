# system_update_7068()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3170–3179 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3170-L3179)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7068()
```

## Documentation

```text
Update {url_alias}.language description.
```

## Code

```php
function system_update_7068() {
  $spec = array(
    'description' => "The language this alias is for; if 'und', the alias will be used for unknown languages. Each Drupal path can have an alias for each supported language.",
    'type' => 'varchar',
    'length' => 12,
    'not null' => TRUE,
    'default' => '',
  );
  db_change_field('url_alias', 'language', 'language', $spec);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
