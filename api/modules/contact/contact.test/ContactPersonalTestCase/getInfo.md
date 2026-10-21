# ContactPersonalTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 306–312 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L306-L312)
- **Class:** [ContactPersonalTestCase](../ContactPersonalTestCase.md)
- **Module/theme:** contact

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
      'name' => 'Personal contact form',
      'description' => 'Tests personal contact form functionality.',
      'group' => 'Contact',
    );
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
