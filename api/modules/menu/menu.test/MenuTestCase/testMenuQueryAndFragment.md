# MenuTestCase::testMenuQueryAndFragment()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 280–295 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L280-L295)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function testMenuQueryAndFragment()
```

## Documentation

```text
Add and remove a menu link with a query string and fragment.
```

## Code

```php
  function testMenuQueryAndFragment() {
    $this->drupalLogin($this->big_user);

    // Make a path with query and fragment on.
    $path = 'node?arg1=value1&arg2=value2';
    $item = $this->addMenuLink(0, $path);

    $this->drupalGet('admin/structure/menu/item/' . $item['mlid'] . '/edit');
    $this->assertFieldByName('link_path', $path, 'Path is found with both query and fragment.');

    // Now change the path to something without query and fragment.
    $path = 'node';
    $this->drupalPost('admin/structure/menu/item/' . $item['mlid'] . '/edit', array('link_path' => $path), t('Save'));
    $this->drupalGet('admin/structure/menu/item/' . $item['mlid'] . '/edit');
    $this->assertFieldByName('link_path', $path, 'Path no longer has query or fragment.');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
