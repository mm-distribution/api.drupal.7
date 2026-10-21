# MenuRouterTestCase::menuLoadRouter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 615–617 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L615-L617)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function menuLoadRouter($router_path)
```

## Documentation

```text
Load the router for a given path.
```

## Code

```php
  protected function menuLoadRouter($router_path) {
    return db_query('SELECT * FROM {menu_router} WHERE path = :path', array(':path' => $router_path))->fetchAssoc();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
