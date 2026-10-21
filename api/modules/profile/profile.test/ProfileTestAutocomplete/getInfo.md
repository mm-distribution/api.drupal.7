# ProfileTestAutocomplete::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 319–325 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L319-L325)
- **Class:** [ProfileTestAutocomplete](../ProfileTestAutocomplete.md)
- **Module/theme:** profile

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Autocompletion',
      'description' => 'Test profile fields with autocompletion.',
      'group' => 'Profile'
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
