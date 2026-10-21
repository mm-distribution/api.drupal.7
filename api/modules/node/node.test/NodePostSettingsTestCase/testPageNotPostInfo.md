# NodePostSettingsTestCase::testPageNotPostInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 916–933 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L916-L933)
- **Class:** [NodePostSettingsTestCase](../NodePostSettingsTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPageNotPostInfo()
```

## Documentation

```text
Confirms absence of post information on a new node.
```

## Code

```php
  function testPageNotPostInfo() {

    // Set "Basic page" content type to display post information.
    $edit = array();
    $edit['node_submitted'] = FALSE;
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));

    // Create a node.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName(8);
    $edit["body[$langcode][0][value]"] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the post information is displayed.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->assertNoRaw('<span class="submitted">', 'Post information is not displayed.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
