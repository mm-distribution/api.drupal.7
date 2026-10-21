# LocaleDateFormatsFunctionalTest::testLocalizeDateFormats()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3047–3089 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3047-L3089)
- **Class:** [LocaleDateFormatsFunctionalTest](../LocaleDateFormatsFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testLocalizeDateFormats()
```

## Documentation

```text
Functional tests for localizing date formats.
```

## Code

```php
  function testLocalizeDateFormats() {
    // Add language.
    $edit = array(
      'langcode' => 'fr',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Set language negotiation.
    $language_type = LANGUAGE_TYPE_INTERFACE;
    $edit = array(
      "{$language_type}[enabled][locale-url]" => TRUE,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Configure date formats.
    $this->drupalGet('admin/config/regional/date-time/locale');
    $this->assertText('Français', 'Configured languages appear.');
    $edit = array(
      'date_format_long' => 'd.m.Y - H:i',
      'date_format_medium' => 'd.m.Y - H:i',
      'date_format_short' => 'd.m.Y - H:i',
    );
    $this->drupalPost('admin/config/regional/date-time/locale/fr/edit', $edit, t('Save configuration'));
    $this->assertText(t('Configuration saved.'), 'French date formats updated.');
    $edit = array(
      'date_format_long' => 'j M Y - g:ia',
      'date_format_medium' => 'j M Y - g:ia',
      'date_format_short' => 'j M Y - g:ia',
    );
    $this->drupalPost('admin/config/regional/date-time/locale/en/edit', $edit, t('Save configuration'));
    $this->assertText(t('Configuration saved.'), 'English date formats updated.');

    // Create node content.
    $node = $this->drupalCreateNode(array('type' => 'article'));

    // Configure format for the node posted date changes with the language.
    $this->drupalGet('node/' . $node->nid);
    $english_date = format_date($node->created, 'custom', 'j M Y');
    $this->assertText($english_date, 'English date format appears');
    $this->drupalGet('fr/node/' . $node->nid);
    $french_date = format_date($node->created, 'custom', 'd.m.Y');
    $this->assertText($french_date, 'French date format appears');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
