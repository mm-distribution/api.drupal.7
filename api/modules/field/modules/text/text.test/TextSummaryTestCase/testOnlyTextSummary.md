# TextSummaryTestCase::testOnlyTextSummary()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 413–426 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L413-L426)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function testOnlyTextSummary()
```

## Documentation

```text
Test sending only summary.
```

## Code

```php
  function testOnlyTextSummary() {
    // Login as article creator.
    $this->drupalLogin($this->article_creator);
    // Create article with summary but empty body.
    $summary = $this->randomName();
    $edit = array(
      "title" => $this->randomName(),
      "body[und][0][summary]" => $summary,
    );
    $this->drupalPost('node/add/article', $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($edit['title']);

    $this->assertIdentical($node->body['und'][0]['summary'], $summary, 'Article with with summary and no body has been submitted.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
