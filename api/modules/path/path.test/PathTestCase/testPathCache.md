# PathTestCase::testPathCache()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 31–51 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L31-L51)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function testPathCache()
```

## Documentation

```text
Tests the path cache.
```

## Code

```php
  function testPathCache() {
    // Create test node.
    $node1 = $this->drupalCreateNode();

    // Create alias.
    $edit = array();
    $edit['source'] = 'node/' . $node1->nid;
    $edit['alias'] = $this->randomName(8);
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    // Visit the system path for the node and confirm a cache entry is
    // created.
    cache_clear_all('*', 'cache_path', TRUE);
    $this->drupalGet($edit['source']);
    $this->assertTrue(cache_get($edit['source'], 'cache_path'), 'Cache entry was created.');

    // Visit the alias for the node and confirm a cache entry is created.
    cache_clear_all('*', 'cache_path', TRUE);
    $this->drupalGet($edit['alias']);
    $this->assertTrue(cache_get($edit['source'], 'cache_path'), 'Cache entry was created.');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
