# NodeMultiByteUtf8Test::testMultiByteUtf8()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 3112–3125 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L3112-L3125)
- **Class:** [NodeMultiByteUtf8Test](../NodeMultiByteUtf8Test.md)
- **Module/theme:** node

## Signature

```php
public function testMultiByteUtf8()
```

## Documentation

```text
Tests that multi-byte UTF-8 characters are stored and retrieved correctly.
```

## Code

```php
  public function testMultiByteUtf8() {
    $connection = Database::getConnection();
    // On MySQL, this test will only run if 'charset' is set to 'utf8mb4' in
    // settings.php.
    if (!($connection->utf8mb4IsSupported() && $connection->utf8mb4IsActive())) {
      return;
    }
    $title = '🐙';
    $this->assertTrue(drupal_strlen($title, 'utf-8') < strlen($title), 'Title has multi-byte characters.');
    $node = $this->drupalCreateNode(array('title' => $title));
    $this->drupalGet('node/' . $node->nid);
    $result = $this->xpath('//h1[@id="page-title"]');
    $this->assertEqual(trim((string) $result[0]), $title, 'The passed title was returned.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
