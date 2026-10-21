# ImageFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 33–42 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L33-L42)
- **Class:** [ImageFieldTestCase](../ImageFieldTestCase.md)
- **Module/theme:** image

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'image';
    parent::setUp($modules);
    $this->admin_user = $this->drupalCreateUser(array('access content', 'access administration pages', 'administer site configuration', 'administer content types', 'administer nodes', 'create article content', 'edit any article content', 'delete any article content', 'administer image styles', 'administer fields'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
