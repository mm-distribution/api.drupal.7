# MenuTestCase::assertMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 546–559 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L546-L559)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function assertMenuLink($mlid, array $expected_item)
```

## Documentation

```text
Fetch the menu item from the database and compare it to the specified
array.

@param $mlid
  Menu item id.
@param $item
  Array containing properties to verify.
```

## Code

```php
  function assertMenuLink($mlid, array $expected_item) {
    // Retrieve menu link.
    $item = db_query('SELECT * FROM {menu_links} WHERE mlid = :mlid', array(':mlid' => $mlid))->fetchAssoc();
    $options = unserialize($item['options']);
    if (!empty($options['query'])) {
      $item['link_path'] .= '?' . drupal_http_build_query($options['query']);
    }
    if (!empty($options['fragment'])) {
      $item['link_path'] .= '#' . $options['fragment'];
    }
    foreach ($expected_item as $key => $value) {
      $this->assertEqual($item[$key], $value, format_string('Parameter %key had expected value.', array('%key' => $key)));
    }
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
