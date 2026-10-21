# ContactSitewideTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 11–17 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L11-L17)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
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
      'name' => 'Site-wide contact form',
      'description' => 'Tests site-wide contact form functionality.',
      'group' => 'Contact',
    );
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
