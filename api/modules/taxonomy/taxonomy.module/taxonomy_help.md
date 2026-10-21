# taxonomy_help()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 19–62 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L19-L62)
- **Module/theme:** taxonomy
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function taxonomy_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function taxonomy_help($path, $arg) {
  switch ($path) {
    case 'admin/help#taxonomy':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Taxonomy module allows you to classify the content of your website. To classify content, you define <em>vocabularies</em> that contain related <em>terms</em>, and then assign the vocabularies to content types. For more information, see the online handbook entry for the <a href="@taxonomy">Taxonomy module</a>.', array('@taxonomy' => 'http://drupal.org/documentation/modules/taxonomy/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Creating vocabularies') . '</dt>';
      $output .= '<dd>' . t('Users with sufficient <a href="@perm">permissions</a> can create <em>vocabularies</em> and <em>terms</em> through the <a href="@taxo">Taxonomy page</a>. The page listing the terms provides a drag-and-drop interface for controlling the order of the terms and sub-terms within a vocabulary, in a hierarchical fashion. A <em>controlled vocabulary</em> classifying music by genre with terms and sub-terms could look as follows:', array('@taxo' => url('admin/structure/taxonomy'), '@perm' => url('admin/people/permissions', array('fragment' => 'module-taxonomy'))));
      $output .= '<ul><li>' . t('<em>vocabulary</em>: Music') . '</li>';
      $output .= '<ul><li>' . t('<em>term</em>: Jazz') . '</li>';
      $output .= '<ul><li>' . t('<em>sub-term</em>: Swing') . '</li>';
      $output .= '<li>' . t('<em>sub-term</em>: Fusion') . '</li></ul></ul>';
      $output .= '<ul><li>' . t('<em>term</em>: Rock') . '</li>';
      $output .= '<ul><li>' . t('<em>sub-term</em>: Country rock') . '</li>';
      $output .= '<li>' . t('<em>sub-term</em>: Hard rock') . '</li></ul></ul></ul>';
      $output .= t('You can assign a sub-term to multiple parent terms. For example, <em>fusion</em> can be assigned to both <em>rock</em> and <em>jazz</em>.') . '</dd>';
      $output .= '<dd>' . t('Terms in a <em>free-tagging vocabulary</em> can be built gradually as you create or edit content. This is often done used for blogs or photo management applications.') . '</dd>';
      $output .= '<dt>' . t('Assigning vocabularies to content types') . '</dt>';
      $output .= '<dd>' . t('Before you can use a new vocabulary to classify your content, a new Taxonomy term field must be added to a <a href="@ctedit">content type</a> on its <em>manage fields</em> page. When adding a taxonomy field, you choose a <em>widget</em> to use to enter the taxonomy information on the content editing page: a select list, checkboxes, radio buttons, or an auto-complete field (to build a free-tagging vocabulary). After choosing the field type and widget, on the subsequent <em>field settings</em> page you can choose the desired vocabulary, whether one or multiple terms can be chosen from the vocabulary, and other settings. The same vocabulary can be added to multiple content types, by using the "Add existing field" section on the manage fields page.', array('@ctedit' => url('admin/structure/types'))) . '</dd>';
      $output .= '<dt>' . t('Classifying content') . '</dt>';
      $output .= '<dd>' . t('After the vocabulary is assigned to the content type, you can start classifying content. The field with terms will appear on the content editing screen when you edit or <a href="@addnode">add new content</a>.', array('@addnode' => url('node/add'))) . '</dd>';
      $output .= '<dt>' . t('Viewing listings and RSS feeds by term') . '</dt>';
      $output .= '<dd>' . t("Each taxonomy term automatically provides a page listing content that has its classification, and a corresponding RSS feed. For example, if the taxonomy term <em>country rock</em> has the ID 123 (you can see this by looking at the URL when hovering on the linked term, which you can click to navigate to the listing page), then you will find this list at the path <em>taxonomy/term/123</em>. The RSS feed will use the path <em>taxonomy/term/123/feed</em> (the RSS icon for this term's listing will automatically display in your browser's address bar when viewing the listing page).") . '</dd>';
      $output .= '<dt>' . t('Extending Taxonomy module') . '</dt>';
      $output .= '<dd>' . t('There are <a href="@taxcontrib">many contributed modules</a> that extend the behavior of the Taxonomy module for both display and organization of terms.', array('@taxcontrib' => 'http://drupal.org/project/modules?filters=tid:71&solrsort=sis_project_release_usage%20desc'));
      $output .= '</dl>';
      return $output;
    case 'admin/structure/taxonomy':
      $output = '<p>' . t('Taxonomy is for categorizing content. Terms are grouped into vocabularies. For example, a vocabulary called "Fruit" would contain the terms "Apple" and "Banana".') . '</p>';
      return $output;
    case 'admin/structure/taxonomy/%':
      $vocabulary = taxonomy_vocabulary_machine_name_load($arg[3]);
      switch ($vocabulary->hierarchy) {
        case 0:
          return '<p>' . t('You can reorganize the terms in %capital_name using their drag-and-drop handles, and group terms under a parent term by sliding them under and to the right of the parent.', array('%capital_name' => drupal_ucfirst($vocabulary->name), '%name' => $vocabulary->name)) . '</p>';
        case 1:
          return '<p>' . t('%capital_name contains terms grouped under parent terms. You can reorganize the terms in %capital_name using their drag-and-drop handles.', array('%capital_name' => drupal_ucfirst($vocabulary->name), '%name' => $vocabulary->name)) . '</p>';
        case 2:
          return '<p>' . t('%capital_name contains terms with multiple parents. Drag and drop of terms with multiple parents is not supported, but you can re-enable drag-and-drop support by editing each term to include only a single parent.', array('%capital_name' => drupal_ucfirst($vocabulary->name))) . '</p>';
      }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
