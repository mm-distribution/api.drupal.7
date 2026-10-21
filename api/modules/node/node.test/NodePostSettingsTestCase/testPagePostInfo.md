# NodePostSettingsTestCase::testPagePostInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 893–911 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L893-L911)
- **Class:** [NodePostSettingsTestCase](../NodePostSettingsTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPagePostInfo()
```

## Documentation

```text
Confirms "Basic page" content type and post information is on a new node.
```

## Code

```php
  function testPagePostInfo() {

    // Set "Basic page" content type to display post information.
    $edit = array();
    $edit['node_submitted'] = TRUE;
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));

    // Create a node.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName(8);
    $edit["body[$langcode][0][value]"] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the post information is displayed.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $elements = $this->xpath('//div[contains(@class,:class)]', array(':class' => 'submitted'));
    $this->assertEqual(count($elements), 1, 'Post information is displayed.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
