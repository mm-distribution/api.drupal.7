# TranslationTestCase::testContentTranslation()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 68–155 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L68-L155)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function testContentTranslation()
```

## Documentation

```text
Creates, modifies, and updates a basic page with a translation.
```

## Code

```php
  function testContentTranslation() {
    // Create Basic page in English.
    $node_title = $this->randomName();
    $node_body =  $this->randomName();
    $node = $this->createPage($node_title, $node_body, 'en');

    // Unpublish the original node to check that this has no impact on the
    // translation overview page, publish it again afterwards.
    $this->drupalLogin($this->admin_user);
    $this->drupalPost('node/' . $node->nid . '/edit', array('status' => FALSE), t('Save'));
    $this->drupalGet('node/' . $node->nid . '/translate');
    $this->drupalPost('node/' . $node->nid . '/edit', array('status' => NODE_PUBLISHED), t('Save'));
    $this->drupalLogin($this->translator);

    // Check that the "add translation" link uses a localized path.
    $languages = language_list();
    $this->drupalGet('node/' . $node->nid . '/translate');
    $this->assertLinkByHref($languages['es']->prefix . '/node/add/' . str_replace('_', '-', $node->type), 0, format_string('The "add translation" link for %language points to the localized path of the target language.', array('%language' => $languages['es']->name)));

    // Submit translation in Spanish.
    $node_translation_title = $this->randomName();
    $node_translation_body = $this->randomName();
    $node_translation = $this->createTranslation($node, $node_translation_title, $node_translation_body, 'es');

    // Check that the "edit translation" and "view node" links use localized
    // paths.
    $this->drupalGet('node/' . $node->nid . '/translate');
    $this->assertLinkByHref($languages['es']->prefix . '/node/' . $node_translation->nid . '/edit', 0, format_string('The "edit" link for the translation in %language points to the localized path of the translation language.', array('%language' => $languages['es']->name)));
    $this->assertLinkByHref($languages['es']->prefix . '/node/' . $node_translation->nid, 0, format_string('The "view" link for the translation in %language points to the localized path of the translation language.', array('%language' => $languages['es']->name)));

    // Attempt to submit a duplicate translation by visiting the node/add page
    // with identical query string.
    $this->drupalGet('node/add/page', array('query' => array('translation' => $node->nid, 'target' => 'es')));
    $this->assertRaw(t('A translation of %title in %language already exists', array('%title' => $node_title, '%language' => $languages['es']->name)), 'Message regarding attempted duplicate translation is displayed.');

    // Attempt a resubmission of the form - this emulates using the back button
    // to return to the page then resubmitting the form without a refresh.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $this->drupalPost('node/add/page', $edit, t('Save'), array('query' => array('translation' => $node->nid, 'language' => 'es')));
    $duplicate = $this->drupalGetNodeByTitle($edit["title"]);
    $this->assertEqual($duplicate->tnid, 0, 'The node does not have a tnid.');

    // Update original and mark translation as outdated.
    $node_body = $this->randomName();
    $node->body[LANGUAGE_NONE][0]['value'] = $node_body;
    $edit = array();
    $edit["body[$langcode][0][value]"] = $node_body;
    $edit['translation[retranslate]'] = TRUE;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertRaw(t('Basic page %title has been updated.', array('%title' => $node_title)), 'Original node updated.');

    // Check to make sure that interface shows translation as outdated.
    $this->drupalGet('node/' . $node->nid . '/translate');
    $this->assertRaw('<span class="marker">' . t('outdated') . '</span>', 'Translation marked as outdated.');

    // Update translation and mark as updated.
    $edit = array();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $edit['translation[status]'] = FALSE;
    $this->drupalPost('node/' . $node_translation->nid . '/edit', $edit, t('Save'));
    $this->assertRaw(t('Basic page %title has been updated.', array('%title' => $node_translation_title)), 'Translated node updated.');

    // Confirm that disabled languages are an option for translators when
    // creating nodes.
    $this->drupalGet('node/add/page');
    $this->assertFieldByXPath('//select[@name="language"]//option', 'it', 'Italian (disabled) is available in language selection.');
    $translation_it = $this->createTranslation($node, $this->randomName(), $this->randomName(), 'it');
    $this->assertRaw($translation_it->body[LANGUAGE_NONE][0]['value'], 'Content created in Italian (disabled).');

    // Confirm that language neutral is an option for translators when there are
    // disabled languages.
    $this->drupalGet('node/add/page');
    $this->assertFieldByXPath('//select[@name="language"]//option', LANGUAGE_NONE, 'Language neutral is available in language selection with disabled languages.');
    $node2 = $this->createPage($this->randomName(), $this->randomName(), LANGUAGE_NONE);
    $this->assertRaw($node2->body[LANGUAGE_NONE][0]['value'], 'Language neutral content created with disabled languages available.');

    // Leave just one language enabled and check that the translation overview
    // page is still accessible.
    $this->drupalLogin($this->admin_user);
    $edit = array('enabled[es]' => FALSE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));
    $this->drupalLogin($this->translator);
    $this->drupalGet('node/' . $node->nid . '/translate');
    $this->assertRaw(t('Translations of %title', array('%title' => $node->title)), 'Translation overview page available with only one language enabled.');
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
