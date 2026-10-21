# PathTestCase::testAdminAlias()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 56–159 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L56-L159)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function testAdminAlias()
```

## Documentation

```text
Tests alias functionality through the admin interfaces.
```

## Code

```php
  function testAdminAlias() {
    // Create test node.
    $node1 = $this->drupalCreateNode();

    // Create alias.
    $edit = array();
    $edit['source'] = 'node/' . $node1->nid;
    $edit['alias'] = $this->randomName(8);
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($edit['alias']);
    $this->assertText($node1->title, 'Alias works.');
    $this->assertResponse(200);

    // Change alias to one containing "exotic" characters.
    $pid = $this->getPID($edit['alias']);

    $previous = $edit['alias'];
    $edit['alias'] = "- ._~!$'\"()*@[]?&+%#,;=:" . // "Special" ASCII characters.
      "%23%25%26%2B%2F%3F" . // Characters that look like a percent-escaped string.
      "éøïвβ中國書۞"; // Characters from various non-ASCII alphabets.
    $this->drupalPost('admin/config/search/path/edit/' . $pid, $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($edit['alias']);
    $this->assertText($node1->title, 'Changed alias works.');
    $this->assertResponse(200);

    drupal_static_reset('drupal_lookup_path');
    // Confirm that previous alias no longer works.
    $this->drupalGet($previous);
    $this->assertNoText($node1->title, 'Previous alias no longer works.');
    $this->assertResponse(404);

    // Create second test node.
    $node2 = $this->drupalCreateNode();

    // Set alias to second test node.
    $edit['source'] = 'node/' . $node2->nid;
    // leave $edit['alias'] the same
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    // Confirm no duplicate was created.
    $this->assertRaw(t('The alias %alias is already in use in this language.', array('%alias' => $edit['alias'])), 'Attempt to move alias was rejected.');

    // Delete alias.
    $this->drupalPost('admin/config/search/path/edit/' . $pid, array(), t('Delete'));
    $this->drupalPost(NULL, array(), t('Confirm'));

    // Confirm that the alias no longer works.
    $this->drupalGet($edit['alias']);
    $this->assertNoText($node1->title, 'Alias was successfully deleted.');
    $this->assertResponse(404);

    // Create third and fourth test node.
    $node3 = $this->drupalCreateNode();
    $node4 = $this->drupalCreateNode();

    // Give the node aliases a common first part.
    $name = $this->randomName(4);

    // Create aliases containing a slash.
    $edit = array();
    $edit['source'] = 'node/' . $node3->nid;
    $alias3 = $name . '/' . $this->randomName(5);
    $edit['alias'] = $alias3;
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));
    $edit['source'] = 'node/' . $node4->nid;
    $alias4 = $name . '/' . $this->randomName(4);
    $edit['alias'] = $alias4;
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    // Confirm that the aliases work.
    $this->drupalGet($alias3);
    $this->assertText($node3->title, 'Alias works.');
    $this->assertResponse(200);
    $this->drupalGet($alias4);
    $this->assertText($node4->title, 'Alias works.');
    $this->assertResponse(200);

    // Confirm that filters containing slashes work.
    $this->drupalGet('admin/config/search/path/list/' . $alias3);
    $this->assertFieldByName('filter', $alias3);
    $this->assertText($alias3, 'Searched-for alias with slash found.');
    $this->assertNoText($alias4, 'Different alias with slash not found.');
    $this->assertResponse(200);

    // Delete aliases.
    $pid = $this->getPID($alias3);
    $this->drupalPost('admin/config/search/path/edit/' . $pid, array(), t('Delete'));
    $this->drupalPost(NULL, array(), t('Confirm'));
    $pid = $this->getPID($alias4);
    $this->drupalPost('admin/config/search/path/edit/' . $pid, array(), t('Delete'));
    $this->drupalPost(NULL, array(), t('Confirm'));

    // Confirm that the aliases no longer work.
    $this->drupalGet($alias3);
    $this->assertNoText($node3->title, 'Alias was successfully deleted.');
    $this->assertResponse(404);
    $this->drupalGet($alias4);
    $this->assertNoText($node4->title, 'Alias was successfully deleted.');
    $this->assertResponse(404);
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
