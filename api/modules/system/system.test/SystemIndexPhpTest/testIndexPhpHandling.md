# SystemIndexPhpTest::testIndexPhpHandling()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3031–3042 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3031-L3042)
- **Class:** [SystemIndexPhpTest](../SystemIndexPhpTest.md)
- **Module/theme:** system

## Signature

```php
function testIndexPhpHandling()
```

## Documentation

```text
Test index.php handling.
```

## Code

```php
  function testIndexPhpHandling() {
    $index_php = $GLOBALS['base_url'] . '/index.php';

    $this->drupalGet($index_php, array('external' => TRUE));
    $this->assertResponse(200, 'Make sure index.php returns a valid page.');

    $this->drupalGet($index_php, array('external' => TRUE, 'query' => array('q' => 'user')));
    $this->assertResponse(200, 'Make sure index.php?q=user returns a valid page.');

    $this->drupalGet($index_php .'/user', array('external' => TRUE));
    $this->assertResponse(404, "Make sure index.php/user returns a 'page not found'.");
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
