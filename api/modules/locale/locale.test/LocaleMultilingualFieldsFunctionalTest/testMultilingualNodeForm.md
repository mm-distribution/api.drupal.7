# LocaleMultilingualFieldsFunctionalTest::testMultilingualNodeForm()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2824–2868 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2824-L2868)
- **Class:** [LocaleMultilingualFieldsFunctionalTest](../LocaleMultilingualFieldsFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testMultilingualNodeForm()
```

## Documentation

```text
Test if field languages are correctly set through the node form.
```

## Code

```php
  function testMultilingualNodeForm() {
    // Create "Basic page" content.
    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $title_value = $this->randomName(8);
    $body_key = "body[$langcode][0][value]";
    $body_value = $this->randomName(16);

    // Create node to edit.
    $edit = array();
    $edit[$title_key] = $title_value;
    $edit[$body_key] = $body_value;
    $edit['language'] = 'en';
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the node exists in the database.
    $node = $this->drupalGetNodeByTitle($edit[$title_key]);
    $this->assertTrue($node, 'Node found in database.');

    $assert = isset($node->body['en']) && !isset($node->body[LANGUAGE_NONE]) && $node->body['en'][0]['value'] == $body_value;
    $this->assertTrue($assert, 'Field language correctly set.');

    // Change node language.
    $this->drupalGet("node/$node->nid/edit");
    $edit = array(
      $title_key => $this->randomName(8),
      'language' => 'it'
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($edit[$title_key]);
    $this->assertTrue($node, 'Node found in database.');

    $assert = isset($node->body['it']) && !isset($node->body['en']) && $node->body['it'][0]['value'] == $body_value;
    $this->assertTrue($assert, 'Field language correctly changed.');

    // Enable content language URL detection.
    language_negotiation_set(LANGUAGE_TYPE_CONTENT, array(LOCALE_LANGUAGE_NEGOTIATION_URL => 0));

    // Test multilingual field language fallback logic.
    $this->drupalGet("it/node/$node->nid");
    $this->assertRaw($body_value, 'Body correctly displayed using Italian as requested language');

    $this->drupalGet("node/$node->nid");
    $this->assertRaw($body_value, 'Body correctly displayed using English as requested language');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
