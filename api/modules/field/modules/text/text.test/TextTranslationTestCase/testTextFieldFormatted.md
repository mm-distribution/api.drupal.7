# TextTranslationTestCase::testTextFieldFormatted()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 500–542 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L500-L542)
- **Class:** [TextTranslationTestCase](../TextTranslationTestCase.md)
- **Module/theme:** text

## Signature

```php
function testTextFieldFormatted()
```

## Documentation

```text
Check that user that does not have access the field format cannot see the
source value when creating a translation.
```

## Code

```php
  function testTextFieldFormatted() {
    // Make node body multiple.
    $edit = array('field[cardinality]' => -1);
    $this->drupalPost('admin/structure/types/manage/article/fields/body', $edit, t('Save settings'));
    $this->drupalGet('node/add/article');
    $this->assertFieldByXPath("//input[@name='body_add_more']", t('Add another item'), 'Body field cardinality set to multiple.');

    $body = array(
      $this->randomName(),
      $this->randomName(),
    );

    // Create an article with the first body input format set to "Full HTML".
    $title = $this->randomName();
    $edit = array(
      'title' => $title,
      'language' => 'en',
    );
    $this->drupalPost('node/add/article', $edit, t('Save'));

    // Populate the body field: the first item gets the "Full HTML" input
    // format, the second one "Filtered HTML".
    $formats = array('full_html', 'filtered_html');
    $langcode = LANGUAGE_NONE;
    foreach ($body as $delta => $value) {
      $edit = array(
        "body[$langcode][$delta][value]" => $value,
        "body[$langcode][$delta][format]" => array_shift($formats),
      );
      $this->drupalPost('node/1/edit', $edit, t('Save'));
      $this->assertText($body[$delta], format_string('The body field with delta @delta has been saved.', array('@delta' => $delta)));
    }

    // Login as translator.
    $this->drupalLogin($this->translator);

    // Translate the article in french.
    $node = $this->drupalGetNodeByTitle($title);
    $this->drupalGet("node/$node->nid/translate");
    $this->clickLink(t('add translation'));
    $this->assertNoText($body[0], format_string('The body field with delta @delta is hidden.', array('@delta' => 0)));
    $this->assertText($body[1], format_string('The body field with delta @delta is shown.', array('@delta' => 1)));
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
