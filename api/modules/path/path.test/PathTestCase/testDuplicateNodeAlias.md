# PathTestCase::testDuplicateNodeAlias()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 258–270 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L258-L270)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function testDuplicateNodeAlias()
```

## Documentation

```text
Tests that duplicate aliases fail validation.
```

## Code

```php
  function testDuplicateNodeAlias() {
    // Create one node with a random alias.
    $node_one = $this->drupalCreateNode();
    $edit = array();
    $edit['path[alias]'] = $this->randomName();
    $this->drupalPost('node/' . $node_one->nid . '/edit', $edit, t('Save'));

    // Now create another node and try to set the same alias.
    $node_two = $this->drupalCreateNode();
    $this->drupalPost('node/' . $node_two->nid . '/edit', $edit, t('Save'));
    $this->assertText(t('The alias is already in use.'));
    $this->assertFieldByXPath("//input[@name='path[alias]' and contains(@class, 'error')]", $edit['path[alias]'], 'Textfield exists and has the error class.');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
