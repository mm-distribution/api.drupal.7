# hook_entity_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 202–271 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L202-L271)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_info()
```

## Documentation

```text
Inform the base system and the Field API about one or more entity types.

Inform the system about one or more entity types (i.e., object types that
can be loaded via entity_load() and, optionally, to which fields can be
attached).

@return
  An array whose keys are entity type names and whose values identify
  properties of those types that the system needs to know about:
  - label: The human-readable name of the type.
  - controller class: The name of the class that is used to load the objects.
    The class has to implement the DrupalEntityControllerInterface interface.
    Leave blank to use the DrupalDefaultEntityController implementation.
  - base table: (used by DrupalDefaultEntityController) The name of the
    entity type's base table.
  - revision table: The name of the entity type's revision table (if any).
  - static cache: (used by DrupalDefaultEntityController) FALSE to disable
    static caching of entities during a page request. Defaults to TRUE.
  - field cache: (used by Field API loading and saving of field data) FALSE
    to disable Field API's persistent cache of field data. Only recommended
    if a higher level persistent cache is available for the entity type.
    Defaults to TRUE.
  - load hook: The name of the hook which should be invoked by
    DrupalDefaultEntityController:attachLoad(), for example 'node_load'.
  - uri callback: The name of an implementation of
    callback_entity_info_uri().
  - label callback: (optional) The name of an implementation of
    callback_entity_info_label(), which returns the label of the entity. The
    entity label is the main string associated with an entity; for example,
    the title of a node or the subject of a comment. If there is an entity
    object property that defines the label, then using the 'label' element of
    the 'entity keys' return value component suffices to provide this
    information (see below). Alternatively, specifying this callback allows
    more complex logic to determine the label of an entity. See also the
    entity_label() function, which implements this logic.
  - language callback: (optional) The name of an implementation of
    callback_entity_info_language(). In most situations, when needing to
    determine this value, inspecting a property named after the 'language'
    element of the 'entity keys' should be enough. The language callback is
    meant to be used primarily for temporary alterations of the property
    value: entity-defining modules are encouraged to always define a
    language property, instead of using the callback as main entity language
    source. In fact not having a language property defined is likely to
    prevent an entity from being queried by language. Moreover, given that
    entity_language() is not necessarily used everywhere it would be
    appropriate, modules implementing the language callback should be aware
    that this might not be always called.
  - fieldable: Set to TRUE if you want your entity type to accept fields
    being attached to it.
  - translation: An associative array of modules registered as field
    translation handlers. Array keys are the module names, array values
    can be any data structure the module uses to provide field translation.
    Any empty value disallows the module to appear as a translation handler.
  - entity keys: (optional) An array describing how the Field API can extract
    the information it needs from the objects of the type. Elements:
    - id: The name of the property that contains the primary id of the
      entity. Every entity object passed to the Field API must have this
      property and its value must be numeric.
    - revision: The name of the property that contains the revision id of
      the entity. The Field API assumes that all revision ids are unique
      across all entities of a type. This entry can be omitted if the
      entities of this type are not versionable. Defaults to an empty string.
    - bundle: The name of the property that contains the bundle name for the
      entity. The bundle name defines which set of fields are attached to
      the entity (e.g. what nodes call "content type"). This entry can be
      omitted if this entity type exposes a single bundle (all entities have
      the same collection of fields). The name of this single bundle will be
      the same as the entity type. Defaults to an empty string.
    - label: The name of the property that contains the entity label. For
      example, if the entity's label is located in $entity->subject, then
      'subject' should be specified here. If complex logic is required to
      build the label, a 'label callback' should be defined instead (see
      the 'label callback' section above for details).
    - language: The name of the property, typically 'language', that contains
      the language code representing the language the entity has been created
      in. This value may be changed when editing the entity and represents
      the language its textual components are supposed to have. If no
      language property is available, the 'language callback' may be used
      instead. This entry can be omitted if the entities of this type are not
      language-aware.
  - bundle keys: An array describing how the Field API can extract the
    information it needs from the bundle objects for this type. This entry
    is required if the 'path' provided in the 'bundles'/'admin' section
    identifies the bundle using a named menu placeholder whose loader
    callback returns an object (e.g., $vocabulary for taxonomy terms, or
    $node_type for nodes). If the path does not include the bundle, or the
    bundle is just a string rather than an automatically loaded object, then
    this can be omitted. Elements:
    - bundle: The name of the property of the bundle object that contains
      the name of the bundle object.
  - bundles: An array describing all bundles for this object type. Keys are
    bundles machine names, as found in the objects' 'bundle' property
    (defined in the 'entity keys' entry above). This entry can be omitted if
    this entity type exposes a single bundle (all entities have the same
    collection of fields). The name of this single bundle will be the same as
    the entity type. Elements:
    - label: The human-readable name of the bundle.
    - uri callback: Same as the 'uri callback' key documented above for the
      entity type, but for the bundle only. When determining the URI of an
      entity, if a 'uri callback' is defined for both the entity type and
      the bundle, the one for the bundle is used.
    - admin: An array of information that allows Field UI pages to attach
      themselves to the existing administration pages for the bundle.
      Elements:
      - path: the path of the bundle's main administration page, as defined
        in hook_menu(). If the path includes a placeholder for the bundle,
        the 'bundle argument' and 'real path' keys below are required.
      - bundle argument: The position of the bundle placeholder in 'path', if
        any.
      - real path: The actual path (no placeholder) of the bundle's main
        administration page. This will be used to generate links.
      - access callback: As in hook_menu(). 'user_access' will be assumed if
        no value is provided.
      - access arguments: As in hook_menu().
  - view modes: An array describing the view modes for the entity type. View
    modes let entities be displayed differently depending on the context.
    For instance, a node can be displayed differently on its own page
    ('full' mode), on the home page or taxonomy listings ('teaser' mode), or
    in an RSS feed ('rss' mode). Modules taking part in the display of the
    entity (notably the Field API) can adjust their behavior depending on
    the requested view mode. An additional 'default' view mode is available
    for all entity types. This view mode is not intended for actual entity
    display, but holds default display settings. For each available view
    mode, administrators can configure whether it should use its own set of
    field display settings, or just replicate the settings of the 'default'
    view mode, thus reducing the amount of display configurations to keep
    track of. Keys of the array are view mode names. Each view mode is
    described by an array with the following key/value pairs:
    - label: The human-readable name of the view mode
    - custom settings: A boolean specifying whether the view mode should by
      default use its own custom field display settings. If FALSE, entities
      displayed in this view mode will reuse the 'default' display settings
      by default (e.g. right after the module exposing the view mode is
      enabled), but administrators can later use the Field UI to apply custom
      display settings specific to the view mode.

@see entity_load()
@see hook_entity_info_alter()
```

## Code

```php
function hook_entity_info() {
  $return = array(
    'node' => array(
      'label' => t('Node'),
      'controller class' => 'NodeController',
      'base table' => 'node',
      'revision table' => 'node_revision',
      'uri callback' => 'node_uri',
      'fieldable' => TRUE,
      'translation' => array(
        'locale' => TRUE,
      ),
      'entity keys' => array(
        'id' => 'nid',
        'revision' => 'vid',
        'bundle' => 'type',
        'language' => 'language',
      ),
      'bundle keys' => array(
        'bundle' => 'type',
      ),
      'bundles' => array(),
      'view modes' => array(
        'full' => array(
          'label' => t('Full content'),
          'custom settings' => FALSE,
        ),
        'teaser' => array(
          'label' => t('Teaser'),
          'custom settings' => TRUE,
        ),
        'rss' => array(
          'label' => t('RSS'),
          'custom settings' => FALSE,
        ),
      ),
    ),
  );

  // Search integration is provided by node.module, so search-related
  // view modes for nodes are defined here and not in search.module.
  if (module_exists('search')) {
    $return['node']['view modes'] += array(
      'search_index' => array(
        'label' => t('Search index'),
        'custom settings' => FALSE,
      ),
      'search_result' => array(
        'label' => t('Search result highlighting input'),
        'custom settings' => FALSE,
      ),
    );
  }

  // Bundles must provide a human readable name so we can create help and error
  // messages, and the path to attach Field admin pages to.
  foreach (node_type_get_names() as $type => $name) {
    $return['node']['bundles'][$type] = array(
      'label' => $name,
      'admin' => array(
        'path' => 'admin/structure/types/manage/%node_type',
        'real path' => 'admin/structure/types/manage/' . str_replace('_', '-', $type),
        'bundle argument' => 4,
        'access arguments' => array('administer content types'),
      ),
    );
  }

  return $return;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_info()".

- [entity_cache_test_dependency_entity_info()](../../simpletest/tests/entity_cache_test_dependency.module/entity_cache_test_dependency_entity_info.md) — `modules/simpletest/tests/entity_cache_test_dependency.module`
- [comment_entity_info()](../../comment/comment.module/comment_entity_info.md) — `modules/comment/comment.module`
- [field_test_entity_info()](../../field/tests/field_test.entity.inc/field_test_entity_info.md) — `modules/field/tests/field_test.entity.inc`
- [node_entity_info()](../../node/node.module/node_entity_info.md) — `modules/node/node.module`
- [system_entity_info()](../system.module/system_entity_info.md) — `modules/system/system.module`
- [taxonomy_entity_info()](../../taxonomy/taxonomy.module/taxonomy_entity_info.md) — `modules/taxonomy/taxonomy.module`
- [user_entity_info()](../../user/user.module/user_entity_info.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
