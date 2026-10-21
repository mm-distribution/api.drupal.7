# TranslationTestCase::testLanguageSwitchLinks()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 160–196 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L160-L196)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function testLanguageSwitchLinks()
```

## Documentation

```text
Checks that the language switch links behave properly.
```

## Code

```php
  function testLanguageSwitchLinks() {
    // Create a Basic page in English and its translations in Spanish and
    // Italian.
    $node = $this->createPage($this->randomName(), $this->randomName(), 'en');
    $translation_es = $this->createTranslation($node, $this->randomName(), $this->randomName(), 'es');
    $translation_it = $this->createTranslation($node, $this->randomName(), $this->randomName(), 'it');

    // Check that language switch links are correctly shown only for enabled
    // languages.
    $this->assertLanguageSwitchLinks($node, $translation_es);
    $this->assertLanguageSwitchLinks($translation_es, $node);
    $this->assertLanguageSwitchLinks($node, $translation_it, FALSE);

    // Check that links to the displayed translation appear only in the language
    // switcher block.
    $this->assertLanguageSwitchLinks($node, $node, FALSE, 'node');
    $this->assertLanguageSwitchLinks($node, $node, TRUE, 'block-locale');

    // Unpublish the Spanish translation to check that the related language
    // switch link is not shown.
    $this->drupalLogin($this->admin_user);
    $edit = array('status' => FALSE);
    $this->drupalPost("node/$translation_es->nid/edit", $edit, t('Save'));
    $this->drupalLogin($this->translator);
    $this->assertLanguageSwitchLinks($node, $translation_es, FALSE);

    // Check that content translation links are shown even when no language
    // negotiation is configured.
    $this->drupalLogin($this->admin_user);
    $edit = array('language[enabled][locale-url]' => FALSE);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));
    $this->resetCaches();
    $edit = array('status' => TRUE);
    $this->drupalPost("node/$translation_es->nid/edit", $edit, t('Save'));
    $this->drupalLogin($this->translator);
    $this->assertLanguageSwitchLinks($node, $translation_es, TRUE, 'node');
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
