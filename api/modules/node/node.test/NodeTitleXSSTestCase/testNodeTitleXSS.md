# NodeTitleXSSTestCase::testNodeTitleXSS()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 810–832 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L810-L832)
- **Class:** [NodeTitleXSSTestCase](../NodeTitleXSSTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTitleXSS()
```

## Documentation

```text
Tests XSS functionality with a node entity.
```

## Code

```php
  function testNodeTitleXSS() {
    // Prepare a user to do the stuff.
    $web_user = $this->drupalCreateUser(array('create page content', 'edit any page content'));
    $this->drupalLogin($web_user);

    $xss = '<script>alert("xss")</script>';
    $title = $xss . $this->randomName();
    $edit = array("title" => $title);

    $this->drupalPost('node/add/page', $edit, t('Preview'));
    $this->assertNoRaw($xss, 'Harmful tags are escaped when previewing a node.');

    $settings = array('title' => $title);
    $node = $this->drupalCreateNode($settings);

    $this->drupalGet('node/' . $node->nid);
    // assertTitle() decodes HTML-entities inside the <title> element.
    $this->assertTitle($edit["title"] . ' | Drupal', 'Title is diplayed when viewing a node.');
    $this->assertNoRaw($xss, 'Harmful tags are escaped when viewing a node.');

    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertNoRaw($xss, 'Harmful tags are escaped when editing a node.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
