# ImageFieldDisplayTestCase::testImageFieldFormattersPrivate()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 960–964 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L960-L964)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFieldFormattersPrivate()
```

## Documentation

```text
Test image formatters on node display for private files.
```

## Code

```php
  function testImageFieldFormattersPrivate() {
    // Remove access content permission from anonymous users.
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array('access content' => FALSE));
    $this->_testImageFieldFormatters('private');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
