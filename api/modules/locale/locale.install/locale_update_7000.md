# locale_update_7000()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 37–53 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L37-L53)
- **Module/theme:** locale
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function locale_update_7000()
```

## Documentation

```text
Add context field index and allow longer location.
```

## Code

```php
function locale_update_7000() {
  db_drop_index('locales_source', 'source');
  db_add_index('locales_source', 'source_context', array(array('source', 30), 'context'));

  // Also drop the 'textgroup_location' index added by the i18nstrings module
  // of the i18n project, which prevents the below schema update from running.
  if (db_index_exists('locales_source', 'textgroup_location')) {
    db_drop_index('locales_source', 'textgroup_location');
  }

  db_change_field('locales_source', 'location', 'location', array(
    'type' => 'text',
    'not null' => FALSE,
    'size' => 'big',
    'description' => 'Drupal path in case of online discovered translations or file path in case of imported strings.',
  ));
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
