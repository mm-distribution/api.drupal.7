# MenuRouterTestCase::testMenuLinkOptions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 556–577 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L556-L577)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuLinkOptions()
```

## Documentation

```text
Test menu link 'options' storage and rendering.
```

## Code

```php
  function testMenuLinkOptions() {
    // Create a menu link with options.
    $menu_link = array(
      'link_title' => 'Menu link options test',
      'link_path' => 'node',
      'module' => 'menu_test',
      'options' => array(
        'attributes' => array(
          'title' => 'Test title attribute',
        ),
        'query' => array(
          'testparam' => 'testvalue',
        ),
      ),
    );
    menu_link_save($menu_link);

    // Load front page.
    $this->drupalGet('node');
    $this->assertRaw('title="Test title attribute"', 'Title attribute of a menu link renders.');
    $this->assertRaw('testparam=testvalue', 'Query parameter added to menu link.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
