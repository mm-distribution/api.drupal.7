# NodeCreationTestCase::testUnpublishedNodeCreation()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 691–705 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L691-L705)
- **Class:** [NodeCreationTestCase](../NodeCreationTestCase.md)
- **Module/theme:** node

## Signature

```php
function testUnpublishedNodeCreation()
```

## Documentation

```text
Create an unpublished node and confirm correct redirect behavior.
```

## Code

```php
  function testUnpublishedNodeCreation() {
    // Set "Basic page" content type to be unpublished by default.
    variable_set('node_options_page', array());
    // Set the front page to the default "node" page.
    variable_set('site_frontpage', 'node');

    // Create a node.
    $edit = array();
    $edit["title"] = $this->randomName(8);
    $edit["body[" . LANGUAGE_NONE . "][0][value]"] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the user was redirected to the home page.
    $this->assertText(t('Welcome to Drupal'), t('The user is redirected to the home page.'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
