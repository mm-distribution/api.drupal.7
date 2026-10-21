# PathTestCase::testNodeAlias()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 164–240 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L164-L240)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function testNodeAlias()
```

## Documentation

```text
Tests alias functionality through the node interfaces.
```

## Code

```php
  function testNodeAlias() {
    // Create test node.
    $node1 = $this->drupalCreateNode();

    // Create alias.
    $edit = array();
    $edit['path[alias]'] = $this->randomName(8);
    $this->drupalPost('node/' . $node1->nid . '/edit', $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($edit['path[alias]']);
    $this->assertText($node1->title, 'Alias works.');
    $this->assertResponse(200);

    // Change alias to one containing "exotic" characters.
    $previous = $edit['path[alias]'];
    $edit['path[alias]'] = "- ._~!$'\"()*@[]?&+%#,;=:" . // "Special" ASCII characters.
      "%23%25%26%2B%2F%3F" . // Characters that look like a percent-escaped string.
      "éøïвβ中國書۞"; // Characters from various non-ASCII alphabets.
    $this->drupalPost('node/' . $node1->nid . '/edit', $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($edit['path[alias]']);
    $this->assertText($node1->title, 'Changed alias works.');
    $this->assertResponse(200);

    // Make sure that previous alias no longer works.
    $this->drupalGet($previous);
    $this->assertNoText($node1->title, 'Previous alias no longer works.');
    $this->assertResponse(404);

    // Create second test node.
    $node2 = $this->drupalCreateNode();

    // Set alias to second test node.
    // Leave $edit['path[alias]'] the same.
    $this->drupalPost('node/' . $node2->nid . '/edit', $edit, t('Save'));

    // Confirm that the alias didn't make a duplicate.
    $this->assertText(t('The alias is already in use.'), 'Attempt to moved alias was rejected.');

    // Delete alias.
    $this->drupalPost('node/' . $node1->nid . '/edit', array('path[alias]' => ''), t('Save'));

    // Confirm that the alias no longer works.
    $this->drupalGet($edit['path[alias]']);
    $this->assertNoText($node1->title, 'Alias was successfully deleted.');
    $this->assertResponse(404);

    // Create third test node.
    $node3 = $this->drupalCreateNode();

    // Create an invalid alias with a leading slash and verify that the slash
    // is removed when the link is generated. This ensures that URL aliases
    // cannot be used to inject external URLs.
    // @todo The user interface should either display an error message or
    //   automatically trim these invalid aliases, rather than allowing them to
    //   be silently created, at which point the functional aspects of this
    //   test will need to be moved elsewhere and switch to using a
    //   programmatically-created alias instead.
    $alias = $this->randomName(8);
    $edit = array('path[alias]' => '/' . $alias);
    $this->drupalPost('node/' . $node3->nid . '/edit', $edit, t('Save'));
    $this->drupalGet('admin/content');
    // This checks the link href before clicking it, rather than using
    // DrupalWebTestCase::assertUrl() after clicking it, because the test
    // browser does not always preserve the correct number of slashes in the
    // URL when it visits internal links; using DrupalWebTestCase::assertUrl()
    // would actually make the test pass unconditionally on the testbot (or
    // anywhere else where Drupal is installed in a subdirectory).
    $link_xpath = $this->xpath('//a[normalize-space(text())=:label]', array(':label' => $node3->title));
    $link_href = (string) $link_xpath[0]['href'];
    $link_prefix = base_path() . (variable_get('clean_url', 0) ? '' : '?q=');
    $this->assertEqual($link_href, $link_prefix . $alias);
    $this->clickLink($node3->title);
    $this->assertResponse(404);
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
