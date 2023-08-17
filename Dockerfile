# Stage 1 - Build the environment for the Haal centraal HR prefill
FROM python:3.10-slim-bullseye AS prefill-haalcentraalhr-build

WORKDIR /app

RUN pip install pip -U
COPY . /app
RUN pip install .


# Stage 2 - Build the production image with the Haal centraal HR prefill
FROM openformulieren/open-forms:latest AS production-build

WORKDIR /app

# Copy the dependencies of the prefill_haalcentraalhr
COPY --from=prefill-haalcentraalhr-build /usr/local/lib/python3.10 /usr/local/lib/python3.10

# Add prefill_haalcentraalhr code to the image
COPY --chown=maykin:root ./prefill_haalcentraalhr /app/src/prefill_haalcentraalhr

USER maykin
