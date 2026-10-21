# TextTranslationTestCase::testTextField()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 471–494 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L471-L494)
- **Class:** [TextTranslationTestCase](../TextTranslationTestCase.md)
- **Module/theme:** text

## Signature

```php
function testTextField()
```

## Documentation

```text
Test that a plaintext textfield widget is correctly populated.
```

## Code

```php
  function testTextField() {
    // Disable text processing for body.
    $edit = array('instance[settings][text_processing]' => 0);
    $this->drupalPost('admin/structure/types/manage/article/fields/body', $edit, t('Save settings'));

    // Login as translator.
    $this->drupalLogin($this->translator);

    // Create content.
    $langcode = LANGUAGE_NONE;
    $body = $this->randomName();
    $edit = array(
      "title" => $this->randomName(),
      "language" => 'en',
      "body[$langcode][0][value]" => $body,
    );

    // Translate the article in french.
    $this->drupalPost('node/add/article', $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->drupalGet("node/$node->nid/translate");
    $this->clickLink(t('add translation'));
    $this->assertFieldByXPath("//textarea[@name='body[$langcode][0][value]']", $body, 'The textfield widget is populated.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
