# PagePreviewTestCase::testPagePreview()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 535–559 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L535-L559)
- **Class:** [PagePreviewTestCase](../PagePreviewTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPagePreview()
```

## Documentation

```text
Checks the node preview functionality.
```

## Code

```php
  function testPagePreview() {
    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $body_key = "body[$langcode][0][value]";
    $term_key = "{$this->field_name}[$langcode]";

    // Fill in node creation form and preview node.
    $edit = array();
    $edit[$title_key] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    $edit[$term_key] = $this->term->tid;
    $this->drupalPost('node/add/page', $edit, t('Preview'));

    // Check that the preview is displaying the title, body, and term.
    $this->assertTitle(t('Preview | Drupal'), 'Basic page title is preview.');
    $this->assertText($edit[$title_key], 'Title displayed.');
    $this->assertText($edit[$body_key], 'Body displayed.');
    $this->assertText($this->term->name, 'Term displayed.');

    // Check that the title, body, and term fields are displayed with the
    // correct values.
    $this->assertFieldByName($title_key, $edit[$title_key], 'Title field displayed.');
    $this->assertFieldByName($body_key, $edit[$body_key], 'Body field displayed.');
    $this->assertFieldByName($term_key, $edit[$term_key], 'Term field displayed.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
