# system_get_date_format()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3688–3690 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3688-L3690)
- **Module/theme:** system

## Signature

```php
function system_get_date_format($dfid)
```

## Documentation

```text
Gets the format details for a particular format ID.

@param $dfid
  A date format ID.

@return
  A date format object with the following properties:
  - dfid: The date format ID.
  - format: The date format string.
  - type: The name of the date type.
  - locked: Whether the date format can be changed or not.
```

## Code

```php
function system_get_date_format($dfid) {
  return db_query('SELECT df.dfid, df.format, df.type, df.locked FROM {date_formats} df WHERE df.dfid = :dfid', array(':dfid' => $dfid))->fetch();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
