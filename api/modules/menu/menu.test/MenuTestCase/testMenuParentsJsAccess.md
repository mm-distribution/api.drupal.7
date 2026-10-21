# MenuTestCase::testMenuParentsJsAccess()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 564–576 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L564-L576)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
public function testMenuParentsJsAccess()
```

## Documentation

```text
Test administrative users other than user 1 can access the menu parents AJAX callback.
```

## Code

```php
  public function testMenuParentsJsAccess() {
    $admin = $this->drupalCreateUser(array('administer menu'));
    $this->drupalLogin($admin);
    // Just check access to the callback overall, the POST data is irrelevant.
    $this->drupalGetAJAX('admin/structure/menu/parents');
    $this->assertResponse(200);

    // Do standard user tests.
    // Login the user.
    $this->drupalLogin($this->std_user);
    $this->drupalGetAJAX('admin/structure/menu/parents');
    $this->assertResponse(403);
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
