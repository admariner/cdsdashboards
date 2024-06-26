from dockerspawner import DockerSpawner, SwarmSpawner, SystemUserSpawner

from .variablemixin import VariableMixin, MetaVariableMixin, Command


class VariableDockerSpawner(DockerSpawner, VariableMixin, metaclass=MetaVariableMixin):
    
    default_presentation_cmd = Command(
        ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main'],
        allow_none=False,
        help="""
        The command to run presentations through jhsingle_native_proxy, can be a string or list.
        Default is ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main']
        for the singleuser Docker images to ensure hooks can run.
        """
    ).tag(config=True)

    def options_from_form(self, formdata):
        """Turn options formdata into user_options"""
        options = super().options_from_form(formdata)
        options = self._postprocess_options_from_form(options)
        return options

class VariableSwarmSpawner(SwarmSpawner, VariableMixin, metaclass=MetaVariableMixin):
    
    default_presentation_cmd = Command(
        ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main'],
        allow_none=False,
        help="""
        The command to run presentations through jhsingle_native_proxy, can be a string or list.
        Default is ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main']
        for the singleuser Docker images to ensure hooks can run.
        """
    ).tag(config=True)


class VariableSystemUserSpawner(SystemUserSpawner, VariableMixin, metaclass=MetaVariableMixin):
    
    default_presentation_cmd = Command(
        ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main'],
        allow_none=False,
        help="""
        The command to run presentations through jhsingle_native_proxy, can be a string or list.
        Default is ['start.sh', 'python3', '-m', 'jhsingle_native_proxy.main']
        for the singleuser Docker images to ensure hooks can run.
        """
    ).tag(config=True)
