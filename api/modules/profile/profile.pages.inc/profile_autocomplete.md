# profile_autocomplete()

- **Type:** Function
- **File:** [`modules/profile/profile.pages.inc`](_file.md), lines 118–136 · [local source](../../../../source/modules/profile/profile.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.pages.inc#L118-L136)
- **Module/theme:** profile

## Signature

```php
function profile_autocomplete($field, $string)
```

## Documentation

```text
Callback to allow autocomplete of profile text fields.
```

## Code

```php
function profile_autocomplete($field, $string) {
  $matches = array();
  $autocomplete_field = (bool) db_query_range("SELECT 1 FROM {profile_field} WHERE fid = :fid AND autocomplete = 1", 0, 1, array(':fid' => $field))->fetchField();
  if ($autocomplete_field) {
    $values = db_select('profile_value')
      ->fields('profile_value', array('value'))
      ->condition('fid', $field)
      ->condition('value', db_like($string) . '%', 'LIKE')
      ->groupBy('value')
      ->orderBy('value')
      ->range(0, 10)
      ->execute()->fetchCol();
    foreach ($values as $value) {
      $matches[$value] = check_plain($value);
    }
  }

  drupal_json_output($matches);
}
```

---
_Drupal 7.103 · [modules/profile/profile.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
